#!/usr/bin/env python3
# -*-coding:utf-8 -*


from Useful.XboxOneController import XboxOneController as Controller
from Useful.useful import control
from Config.topic_turtleBot import topicMaximas, topicName
import rospy
from geometry_msgs.msg import Twist

middleValues = {
	"TX": (topicMaximas["TX"]["M"] + topicMaximas["TX"]["m"])/2,
	"TY": (topicMaximas["TY"]["M"] + topicMaximas["TY"]["m"])/2,
	"TZ": (topicMaximas["TZ"]["M"] + topicMaximas["TZ"]["m"])/2,
	"RX": (topicMaximas["RX"]["M"] + topicMaximas["RX"]["m"])/2,
	"RY": (topicMaximas["RY"]["M"] + topicMaximas["RY"]["m"])/2,
	"RZ": (topicMaximas["RZ"]["M"] + topicMaximas["RZ"]["m"])/2
}

centralValues = {
	"TX-": middleValues["TX"] + (topicMaximas["TX"]["m"] - middleValues["TX"])/5,
	"TX+": middleValues["TX"] + (topicMaximas["TX"]["M"] - middleValues["TX"])/5,

	"TY-": middleValues["TY"] + (topicMaximas["TY"]["m"] - middleValues["TY"])/5,
	"TY+": middleValues["TY"] + (topicMaximas["TY"]["M"] - middleValues["TY"])/5,

	"TZ-": middleValues["TZ"] + (topicMaximas["TZ"]["m"] - middleValues["TZ"])/5,
	"TZ+": middleValues["TZ"] + (topicMaximas["TZ"]["M"] - middleValues["TZ"])/5,

	"RX-": middleValues["RX"] + (topicMaximas["RX"]["m"] - middleValues["RX"])/5,
	"RX+": middleValues["RX"] + (topicMaximas["RX"]["M"] - middleValues["RX"])/5,

	"RY-": middleValues["RY"] + (topicMaximas["RY"]["m"] - middleValues["RY"])/5,
	"RY+": middleValues["RY"] + (topicMaximas["RY"]["M"] - middleValues["RY"])/5,

	"RZ-": middleValues["RZ"] + (topicMaximas["RZ"]["m"] - middleValues["RZ"])/5,
	"RZ+": middleValues["RZ"] + (topicMaximas["RZ"]["M"] - middleValues["RZ"])/5
}


if __name__ == '__main__':
	try:
		print("Connection...")
		rospy.init_node('XboxOneController', anonymous=False)
		print("Connected !")
		pub = rospy.Publisher(topicName, Twist, queue_size = 5)

		twist = Twist()
		twist.linear.x = middleValues["TX"]
		twist.linear.y = middleValues["TY"]
		twist.linear.z = middleValues["TZ"]
		twist.angular.x = middleValues["RX"]
		twist.angular.y = middleValues["RY"]
		twist.angular.z = middleValues["RZ"]
		pub.publish(twist)

		controller = Controller(
			SLU = topicMaximas["TX"]["M"],
			SLD = topicMaximas["TX"]["m"],
			SRL = topicMaximas["RZ"]["m"],
			SRR = topicMaximas["RZ"]["M"]
		)
		controller.start()

		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			twist.linear.x = control(controller["SL"][1], centralValues["TX-"], centralValues["TX+"], middleValues["TX"])
			twist.linear.y = control(middleValues["TY"], centralValues["TY-"], centralValues["TY+"], middleValues["TY"])
			twist.linear.z = control(middleValues["TZ"], centralValues["TZ-"], centralValues["TZ+"], middleValues["TZ"])
			twist.angular.x = control(middleValues["RX"], centralValues["RX-"], centralValues["RX+"], middleValues["RX"])
			twist.angular.y = control(middleValues["RY"], centralValues["RY-"], centralValues["RY+"], middleValues["RY"])
			twist.angular.z = control(controller["SR"][0], centralValues["RZ-"], centralValues["RZ+"], middleValues["RZ"])
			pub.publish(twist)
			rate.sleep()
	finally:
		controller.stop()
