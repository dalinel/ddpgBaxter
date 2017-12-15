#!/usr/bin/env python
import sys
import rospy
import numpy as np
from geometry_msgs.msg import Pose, PoseStamped
from sensor_msgs.msg import JointState, Image
from std_msgs.msg import *
from control_msgs.msg import JointTrajectoryControllerState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from tf import TransformListener
import math

global reset_bool
reset_bool = False
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
    
        self.left_positions =[0,0,0,0,0,0,0,0]
        self.left_positions =[0,0,0,0,0,0,0,0]
        self.right_joints_pos = []
        self.left_joints_pos = []
        self.right_joints_vel = []
        self.left_joints_vel = []

        self.pub = rospy.Publisher('/yumi/joint_trajectory_vel_controller/command', JointTrajectory, queue_size=1)
        self.js = JointState()
        self.jt = JointTrajectory()
        self.js.header = Header()
        self.jt.header = Header()
        self.js.name = self.left_joint_names + self.right_joint_names
        self.jt.joint_names = self.left_joint_names[0:-1] + self.right_joint_names[0:-1]
        self.js.velocity = []
        self.js.effort = []
        self.sub = rospy.Subscriber('/yumi/joint_trajectory_vel_controller/state', JointTrajectoryControllerState, self.jointTrajectoryControllerStateCB)
        #self.destPos = np.random.uniform(0,0.25, size =(3))
        self.destPos = np.array([ 0.4,  -0.4,  0.25])
        self.reset()

    def jointTrajectoryControllerStateCB(self,msg):
        global reset_bool
        temp_dict = dict(zip(msg.joint_names, msg.actual.positions))
        self.right_joints_pos = [temp_dict[x] for x in self.right_joint_names[0:-1]]
        self.right_joints_pos = self.right_joints_pos + [0]
        self.left_joints_pos = [temp_dict[x] for x in self.left_joint_names[0:-1]]
        self.left_joints_pos = self.left_joints_pos + [0]
        self.jt.points = [JointTrajectoryPoint()]
        if(reset_bool):
            self.jt.points[0].positions=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        else :
            self.jt.points[0].positions= self.left_joints_pos[0:-1] + self.right_joints_pos[0:-1]
            self.jt.points[0].velocities = self.left_positions[0:-1] + self.right_positions[0:-1]


         #self.jt.points[0].positions= self.left_positions[0:-1] + self.right_positions[0:-1]
        #self.jt.points[0].velocities = [0,0,0,0,0,0,0,0.3,0,0,0,0,0,0]

        self.jt.points[0].time_from_start =rospy.Duration(1)


        self.pub.publish(self.jt)

    def getCurrentJointValues(self):
        return self.right_joints_pos

    def getCurrentPose(self):
        self.tf.waitForTransform("/world","/gripper_r_finger_r",rospy.Time(),rospy.Duration(10))
        t = self.tf.getLatestCommonTime("/world", "/gripper_r_finger_r")
        position, quaternion = self.tf.lookupTransform("/world","/gripper_r_finger_r",t)
        print("Gripper pos", position)
        return [position[0],position[1],position[2]]

    def setJointValues(self,tjv):
        self.right_positions = tjv
        self.right_positions[-1] = 0 #close gripper
        rospy.sleep(0.20)
        return True

    def getDist(self):
        position = self.getCurrentPose()
        currentPos = np.array((position[0],position[1],position[2]))
        return np.linalg.norm(currentPos-self.destPos)

    def reset(self):
        global reset_bool
        self.setJointValues(np.random.uniform(-1,1, size=(8)).tolist())
        #self.left_positions = [-2.01081820427463881, 1.4283937236421274, -1.3593418228836045, -0.19315625641494183, 1.7016501799872579, 0.6573540231496411, 3.404315594906305, 0.0]
        self.left_positions =[0,0,0,0,0,0,0,0]
        #self.right_positions = [0.01081820427463881, 2.4283937236421274, 0.3593418228836045, -0.19315625641494183, 1.7016501799872579, 0.6573540231496411, 3.404315594906305, 1.8145107750466565]
        self.right_positions =[0,0,0,0,0,0,0,0]
        reset_bool = True
        #print("1111111111 ", (abs(np.linalg.norm(np.subtract(self.right_joints_pos,self.right_positions)))))
        while((abs(np.linalg.norm(np.subtract(self.right_joints_pos,self.right_positions)))>0.01)):
            rospy.sleep(0.1)
        reset_bool = False

        #print self.destPos
        #self.destPos = np.random.uniform(0,0.25, size =(3))
        self.destPos = np.array([ 0.4,  -0.4,  0.25])
        #print self.destPos
        tjv = self.getCurrentJointValues()
        positions = self.getCurrentPose()
        return tjv+positions+self.destPos.tolist()

    def step(self,vals):
        #print("Destination : ",self.destPos)
        done = False
        prevDist = self.getDist()
        #tjv = [x + y for x,y in zip(vals.flatten().tolist(),self.getCurrentJointValues())]
        tjv = vals.flatten().tolist()
        #print(tjv)
        status = self.setJointValues(tjv)
        curDist = self.getDist()
        #reward = -1
        #if(curDist < prevDist):
        #    reward = 1
        reward = -curDist - 0.00*np.linalg.norm(vals) - 0.5*math.log10(curDist)
        #reward =  -math.log(curDist)
        print("DISTANCE ", curDist)
        #print  self.destPos, -curDist - 0.5*math.log10(curDist) ,-curDist, np.linalg.norm(vals)
        if curDist < 0.01:
            reward = 100
            done = True
        tjv = self.getCurrentJointValues()
        positions = self.getCurrentPose()
        #print("GRIPPER POSE", positions)
        return [curDist,tjv+positions+self.destPos.tolist(), reward, done]

    def done(self):
        self.sub.unregister()
        rospy.signal_shutdown("done")

if __name__ == "__main__":
            r = robotGame()
            print r.getCurrentJointValues()
            print r.getCurrentPose()
            r.reset()
            print r.getCurrentJointValues()
            print r.getCurrentPose()
