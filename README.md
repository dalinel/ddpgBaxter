# ddpgBaxter
This project aim at using the DDPG alogorithm in order to solve a simple graping problem with Baxter.

## Setup info
	*Ros kinetic
	*Baxter simulator: http://sdk.rethinkrobotics.com/wiki/Simulator_Installation
	*Keras 1.2.2
	*Tensorflow
	*CUDA 8 - CUDNN 6 for training

Rq : a contact sensor has been added to baxter's left gripper check the file in
/src/baxter_common/rethink_ee_description/urdf/electric_gripper/fingers/extended_narrow.xacro

##  Done using :
	*https://github.com/robosamir/ddpg-ros-keras
	*https://robosamir.github.io/DDPG-on-a-Real-Robot/
	*https://yanpanlau.github.io/2016/10/11/Torcs-Keras.html

The approach from https://robosamir.github.io/DDPG-on-a-Real-Robot/ has been adapted in order to control the speed of the robot and not the position

## How to use:
roslaunch baxter_sim_examples baxter_ddpg.launch
rosrun ddpg ddpg
Rq in ddpd use play(0) for replay and play(1) for training

## Project status
Reaching the cube ok

