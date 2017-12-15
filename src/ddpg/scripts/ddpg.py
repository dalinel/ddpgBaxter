#!/usr/bin/env python
import numpy as np
import random
from keras.models import model_from_json, Model
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import Adam
import tensorflow as tf
from keras.engine.training import *
import json
import os
from ReplayBuffer import ReplayBuffer
from ActorNetwork import ActorNetwork
from CriticNetwork import CriticNetwork
from new_robotGame import robotGame
import time
from tempfile import TemporaryFile

path="/home/eloise/catkin-ws/src/ddpg/scripts/"
def init(env):
    train_indicator=0
    BUFFER_SIZE = 2000
    BATCH_SIZE = 32
    GAMMA = 0.99
    TAU = 0.001     #Target Network HyperParameters
    LRA = 0.0001    #Learning rate for Actor
    LRC = 0.001     #Lerning rate for Critic

    action_dim = 8  #num of joints being controlled
    state_dim = 18  #num of features in state

    EXPLORE = 200.0*50
    episode_count = 4000 if (train_indicator) else 1
    resultArray=np.zeros((episode_count,2))
    max_steps = 50
    reward = 0
    done = False
    step = 0
    epsilon = 0.3 if (train_indicator) else 0.0
    indicator = 0

    #Tensorflow GPU optimization
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)
    from keras import backend as K
    K.set_session(sess)


    actor = ActorNetwork(sess, state_dim, action_dim, BATCH_SIZE, TAU, LRA)
    critic = CriticNetwork(sess, state_dim, action_dim, BATCH_SIZE, TAU, LRC)
    buff = ReplayBuffer(BUFFER_SIZE)    #Create replay buffer


    #Now load the weight
    print("Now we load the weight")
    try:
        actor.model.load_weights(path+"actormodel.h5")
        critic.model.load_weights(path+"criticmodel.h5")
        actor.target_model.load_weights(path+"actormodel.h5")
        critic.target_model.load_weights(path+"criticmodel.h5")
        print("Weight load successfully")
    except:
        print("Cannot find the weight")

    for i in range(episode_count):

        #print("Episode : " + str(i) + " Replay Buffer " + str(buff.count()))

        ob = env.reset()
        if not train_indicator:
            print "start recording now"
        s_t = np.array(ob)

        total_reward = 0.
        for j in range(max_steps):
            loss = 0
            epsilon -= 0.3 / EXPLORE
            a_t = np.zeros([1,action_dim])
            noise_t = np.zeros([1,action_dim])

            if np.random.random() > epsilon:
                a_type = "Exploit"
                #print(a_t)
                a_t = actor.model.predict(s_t.reshape(1, s_t.shape[0]))*1 #rescale

            else:
                a_type = "Explore"
                a_t = np.random.uniform(-1,1, size=(1,action_dim))

            dist,ob, r_t, done = env.step(a_t)

            s_t1 = np.array(ob)
            #print("a_t ", a_t)

            buff.add(s_t, a_t[0], r_t, s_t1, done)      #Add replay buffer

            #Do the batch update
            batch = buff.getBatch(BATCH_SIZE)
            states = np.asarray([e[0] for e in batch])
            actions = np.asarray([e[1] for e in batch])
            rewards = np.asarray([e[2] for e in batch])
            new_states = np.asarray([e[3] for e in batch])
            dones = np.asarray([e[4] for e in batch])
            y_t = np.asarray([e[1] for e in batch])

            target_q_values = critic.target_model.predict([new_states, actor.target_model.predict(new_states)])

            for k in range(len(batch)):
                if dones[k]:
                    y_t[k] = rewards[k]
                else:
                    y_t[k] = rewards[k] + GAMMA*target_q_values[k]


            total_reward += r_t
            s_t = s_t1


            step += 1
            if done:
                break

     
    print("Init Finish.")
    return ob
    

#path ="/media/dalinel/Maxtor/ddpg/"
def playGame(train_indicator=0):    #1 means Train, 0 means simply Run
    BUFFER_SIZE = 2000
    BATCH_SIZE = 32
    GAMMA = 0.99
    TAU = 0.001     #Target Network HyperParameters
    LRA = 0.0001    #Learning rate for Actor
    LRC = 0.001     #Lerning rate for Critic

    action_dim = 8  #num of joints being controlled
    state_dim = 18  #num of features in state

    EXPLORE = 200.0*50
    episode_count = 4000 if (train_indicator) else 1
    resultArray=np.zeros((episode_count,2))
    max_steps = 50
    reward = 0
    done = False
    step = 0
    epsilon = 0.3 if (train_indicator) else 0.0
    indicator = 0

    #Tensorflow GPU optimization
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)
    from keras import backend as K
    K.set_session(sess)
    if(train_indicator == 1):
        K.set_learning_phase(1)

    actor = ActorNetwork(sess, state_dim, action_dim, BATCH_SIZE, TAU, LRA)
    critic = CriticNetwork(sess, state_dim, action_dim, BATCH_SIZE, TAU, LRC)
    buff = ReplayBuffer(BUFFER_SIZE)    #Create replay buffer

    # Generate a Torcs environment
    env = robotGame()

    #Now load the weight
    print("Now we load the weight")
    try:
        actor.model.load_weights(path+"actormodel.h5")
        critic.model.load_weights(path+"criticmodel.h5")
        actor.target_model.load_weights(path+"actormodel.h5")
        critic.target_model.load_weights(path+"criticmodel.h5")
        print("Weight load successfully")
    except:
        print("Cannot find the weight")

    for i in range(episode_count):

        #print("Episode : " + str(i) + " Replay Buffer " + str(buff.count()))

        ob = init(env)
        if not train_indicator:
            print "start recording now"
        s_t = np.array(ob)

        total_reward = 0.
        for j in range(max_steps):
            loss = 0
            epsilon -= 0.3 / EXPLORE
            a_t = np.zeros([1,action_dim])
            noise_t = np.zeros([1,action_dim])

            if np.random.random() > epsilon:
                a_type = "Exploit"
                #print(a_t)
                a_t = actor.model.predict(s_t.reshape(1, s_t.shape[0]))*1 #rescale

            else:
                a_type = "Explore"
                a_t = np.random.uniform(-1,1, size=(1,action_dim))

            dist,ob, r_t, done = env.step(a_t)

            s_t1 = np.array(ob)
            #print("a_t ", a_t)

            buff.add(s_t, a_t[0], r_t, s_t1, done)      #Add replay buffer

            #Do the batch update
            batch = buff.getBatch(BATCH_SIZE)
            states = np.asarray([e[0] for e in batch])
            actions = np.asarray([e[1] for e in batch])
            rewards = np.asarray([e[2] for e in batch])
            new_states = np.asarray([e[3] for e in batch])
            dones = np.asarray([e[4] for e in batch])
            y_t = np.asarray([e[1] for e in batch])

            target_q_values = critic.target_model.predict([new_states, actor.target_model.predict(new_states)])

            for k in range(len(batch)):
                if dones[k]:
                    y_t[k] = rewards[k]
                else:
                    y_t[k] = rewards[k] + GAMMA*target_q_values[k]

            if (train_indicator):
                loss += critic.model.train_on_batch([states,actions], y_t)
                a_for_grad = actor.model.predict(states)
                grads = critic.gradients(states, a_for_grad)
                actor.train(states, grads)
                actor.target_train()
                critic.target_train()

            total_reward += r_t
            s_t = s_t1

            print("Episode", i, "Step", step, "Action", a_type, "Reward", r_t, "Loss", loss, "Epsilon", epsilon)

            step += 1
            if done:
                break

        if np.mod(i, 50) == 0:
            if (train_indicator):
                print("Now we save model")
                actor.model.save_weights(path+"/weights/actormodel_"+str(i)+".h5", overwrite=True)
                critic.model.save_weights(path+"/weights/criticmodel_"+str(i)+".h5", overwrite=True)

        print("TOTAL REWARD @ " + str(i) +"-th Episode  : Reward " + str(total_reward))
        print("Total Step: " + str(step))
        print("")
        resultArray[i][0]=total_reward
        resultArray[i][1]=dist
        np.savetxt(path+'results.txt', resultArray)
        np.save(path+'results.npy', resultArray)
        actor.model.save_weights(path+"/weights/actormodel_"+".h5", overwrite=True)
        critic.model.save_weights(path+"/weights/criticmodel_"+".h5", overwrite=True)
       

    env.done()
    print("Finish.")





if __name__ == "__main__":
    playGame(1)