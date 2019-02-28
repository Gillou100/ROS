#!/usr/bin/env python3
# -*-coding:utf-8 -*


from Useful.XboxOneController import XboxOneController as Controller
from Useful.useful import control
from Config.topic_turtleBot import topicName, topicMaximas, middleValues, centralValues, stopPosition
import rospy
from geometry_msgs.msg import Twist
from copy import deepcopy

if __name__ == '__main__':
	try:
		print("Connection...")
		rospy.init_node('XboxOneController', anonymous=False)
		print("Connected !")
		pub = rospy.Publisher(topicName, Twist, queue_size = 5)
		pub.publish(stopPosition)

		twist = deepcopy(stopPosition)

		controller = Controller(
			SLU = topicMaximas["TX"]["forward"],
			SLD = topicMaximas["TX"]["backward"],
			SRL = topicMaximas["RZ"]["twist left"],
			SRR = topicMaximas["RZ"]["twist right"]
		)
		controller.start()

		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			if controller["A"]:
				pub.publish(stopPosition)
			else:
				twist.linear.x = control(controller["SL"]["V"], centralValues["TX"][0], centralValues["TX"][1], middleValues["TX"])
				twist.angular.z = control(controller["SR"]["H"], centralValues["RZ"][0], centralValues["RZ"][1], middleValues["RZ"])
				pub.publish(twist)
			rate.sleep()
	finally:
		controller.stop()
