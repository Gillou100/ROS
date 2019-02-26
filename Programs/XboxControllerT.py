#!/usr/bin/env python3
# -*-coding:utf-8 -*


from Useful.XboxOneController import XboxOneController as Controller
from Useful.useful import control
from Config.topic_turtleBot import topicName, topicMaximas, middleValues, stopPosition
import rospy
from geometry_msgs.msg import Twist


if __name__ == '__main__':
	try:
		print("Connection...")
		rospy.init_node('XboxOneController', anonymous=False)
		print("Connected !")
		pub = rospy.Publisher(topicName, Twist, queue_size = 5)
		pub.publish(stopPosition)

		twist = Twist()
		twist.linear.x = middleValues["TX"]
		twist.linear.y = middleValues["TY"]
		twist.linear.z = middleValues["TZ"]
		twist.angular.x = middleValues["RX"]
		twist.angular.y = middleValues["RY"]
		twist.angular.z = middleValues["RZ"]

		controller = Controller(
			SLU = topicMaximas["TX"]["M"],
			SLD = topicMaximas["TX"]["m"],
			SRL = topicMaximas["RZ"]["M"],
			SRR = topicMaximas["RZ"]["m"]
		)
		controller.start()

		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			if controller["A"]:
				pub.publish(stopPosition)
			else:
				twist.linear.x = control(controller["SL"][1], centralValues["TX-"], centralValues["TX+"], middleValues["TX"])
				twist.linear.y = middleValues["TY"]
				twist.linear.z = middleValues["TZ"]
				twist.angular.x = middleValues["RX"]
				twist.angular.y = middleValues["RY"]
				twist.angular.z = control(controller["SR"][0], centralValues["RZ-"], centralValues["RZ+"], middleValues["RZ"])
				pub.publish(twist)
			rate.sleep()
	finally:
		controller.stop()
