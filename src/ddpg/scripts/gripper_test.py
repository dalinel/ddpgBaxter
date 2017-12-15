#!/usr/bin/env python
import baxter_interface
import rospy



rospy.init_node("grippertestelo")
rate = rospy.Rate(10)

gripper = baxter_interface.Gripper("left")
while not rospy.is_shutdown():
    gripper.command_position(100)
    print(gripper.gripping())
    rate.sleep()