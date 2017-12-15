#!/usr/bin/env python
import sys
import rospy
import numpy as np
import baxter_interface
from geometry_msgs.msg import Pose, PoseStamped
from sensor_msgs.msg import JointState, Image
from std_msgs.msg import *
from control_msgs.msg import JointTrajectoryControllerState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from baxter_core_msgs.msg import JointCommand
from baxter_core_msgs.msg import EndpointState
from baxter_core_msgs.msg import EndEffectorState
from gazebo_msgs.msg import ContactsState
from tf import TransformListener
import math

from gazebo_msgs.srv import (
    GetModelState
)


class robotGame():
    def __init__(self):
        #init code
        rospy.init_node("robotGame")
        self.currentDist = 1
        self.previousDist = 1
        self.reached = False
        self.tf = TransformListener()

        self.left_joint_names = ['left_e0', 'left_e1', 'left_s0', 'left_s1', 'left_w0', 'left_w1', 'left_w2']
        self.right_joint_names = ['right_e0', 'right_e1', 'right_s0', 'right_s1', 'right_w0', 'right_w1', 'right_w2']
        
        self.left_joint_positions = [0,0,0,0,0,0,0]
        self.right_joint_positions = [0,0,0,0,0,0,0]
        self.left_joint_speeds = [0,0,0,0,0,0,0]
        self.left_gripper_position_command = 100
        self.left_gripper_force = 0
        self.right_gripper_force = 0
        self.grasp_count = 0
        self.learn_grasp = False
        self.left_endpoint_position = [0,0,0]
        self.right_endpoint_position = [0,0,0]

        self.left_limb_joint_command = JointCommand()
        self.left_gripper =  baxter_interface.Gripper("left")
    
        self.pub = rospy.Publisher('/robot/limb/left/joint_command', JointCommand, queue_size=1)
        self.pub2 = rospy.Publisher('/ddpg/reset', JointCommand, queue_size=1)
        self.sub = rospy.Subscriber('/robot/joint_states', JointState , self.jointStateCB)
        self.sub2 = rospy.Subscriber('/robot/limb/left/endpoint_state', EndpointState , self.left_endpoint_positionCB)
        self.sub3 = rospy.Subscriber("/l_gripper_l_finger_bumper_vals", ContactsState , self.left_gripper_stateCB)
        self.sub4 = rospy.Subscriber("/l_gripper_r_finger_bumper_vals", ContactsState , self.right_gripper_stateCB)    

        self.isResetting = False
        self.destPos = np.array([0.7, 0.15, -0.12+0.025])
        self.destObj = np.array([0.7, 0.10, 0])
        self.reset()

    def jointStateCB(self,msg):
        global reset_bool

        temp_dict = dict(zip(msg.name, msg.position))
        self.left_joint_positions = [temp_dict[x] for x in self.left_joint_names]
        
        self.left_limb_joint_command.mode = 2
        self.left_limb_joint_command.names = self.left_joint_names
        self.left_limb_joint_command.command=self.left_joint_speeds
        if(self.isResetting == False):
            self.pub.publish(self.left_limb_joint_command)
            self.left_gripper.command_position(self.left_gripper_position_command)

    def left_endpoint_positionCB(self,msg):
        self.left_endpoint_position = [msg.pose.position.x, msg.pose.position.y, msg.pose.position.z]
        
    def left_gripper_stateCB(self,msg):
    	if(msg.states != []):
        	self.left_gripper_force = msg.states[0].total_wrench.force.x
        else:
        	self.left_gripper_force = 0
    def right_gripper_stateCB(self,msg):
    	if(msg.states != []):
        	self.right_gripper_force = msg.states[0].total_wrench.force.x
        else:
        	self.right_gripper_force = 0



    def getCurrentJointValues(self):
        return self.left_joint_positions

    def getCurrentPose(self):
        return self.left_endpoint_position


    def setJointValues(self,tjv):
        self.left_joint_speeds = tjv
        rospy.sleep(0.20)
        return True

    def getDist(self):
    	rospy.wait_for_service('/gazebo/get_model_state')
    	try:
        	object_state_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        	object_state = object_state_srv("block", "world")
        	self.destPos = np.array([object_state.pose.position.x, object_state.pose.position.y, object_state.pose.position.z-0.9+0.025])
    	except rospy.ServiceException, e:
    		rospy.logerr("Spawn URDF service call failed: {0}".format(e))
        
        position = self.getCurrentPose()
        currentPos = np.array((position[0],position[1],position[2]))
        return np.linalg.norm(currentPos-self.destPos)

    def reset(self):
        self.isResetting = True
        self.pub2.publish(self.left_limb_joint_command)
        rospy.sleep(15)
        #rospy.wait_for_message("/ddpg/reset2", JointCommand)
        tjv = self.getCurrentJointValues()
        positions = self.getCurrentPose()
        self.learn_grasp = False
        self.grasp_count = 0
        self.isResetting = False
        return tjv+positions+self.destPos.tolist()+self.destObj.tolist()+[self.left_gripper_force, self.right_gripper_force]

    def step(self,vals):

        done = False
        prevDist = self.getDist()

        tjv = vals.flatten().tolist()
        self.left_gripper_position_command = (tjv[-1] +1)*50

        

        tjv = tjv[:-1]

        status = self.setJointValues(tjv)
        curDist = self.getDist()

        reward =-curDist
        if(curDist<0.05):
            done = True
            reward = 100
        #b =-0.0001*self.left_gripper_force*self.right_gripper_force*(1/curDist)
        #a = np.log10(np.linalg.norm(self.destObj-self.destPos)+0.9)
        #if(np.linalg.norm(self.destObj-self.destPos)<0.05):
        #    done = True
        #    reward = 100
        #a = -self.left_gripper_force+self.right_gripper_force

        tjv = self.getCurrentJointValues()
        positions = self.getCurrentPose()
        print(" ")
        print("DISTANCE : ", curDist)
        print("TOTAL REWARD : ", reward)
        print("REWARD move toward obj : ", -2*np.log10(curDist+0.85))
        print("REWARD move obj : ", -np.log10(np.linalg.norm(self.destObj-self.destPos)+0.9))
        
        return [curDist,tjv+positions+self.destPos.tolist()+self.destObj.tolist()+[self.left_gripper_force, self.right_gripper_force], reward, done]

    def done(self):
        self.sub.unregister()
        self.sub2.unregister()
        rospy.signal_shutdown("done")

if __name__ == "__main__":
            r = robotGame()
            print r.getCurrentJointValues()
            print r.getCurrentPose()
            r.reset()
            print r.getCurrentJointValues()
            print r.getCurrentPose()
