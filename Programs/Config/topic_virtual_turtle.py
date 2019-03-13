#!/usr/bin/env python3
# -*-coding:utf-8 -*


from geometry_msgs.msg import Twist
import rospy


topicName = '/turtle1/cmd_vel'

maximasValues = {
	"forward" : 2,
	"backward" : -2,
	"twist left" : 2,
	"twist right" : -2
}
stopValues = {
	"transversal": (maximasValues["forward"] + maximasValues["backward"])/2,
	"yaw": (maximasValues["twist left"] + maximasValues["twist right"])/2,
}
minValues = {
	"forward": stopValues["transversal"] + (maximasValues["forward"] - stopValues["transversal"])/5,
	"backward": stopValues["transversal"] + (maximasValues["backward"] - stopValues["transversal"])/5,
	"twist left": stopValues["yaw"] + (maximasValues["twist left"] - stopValues["yaw"])/5,
	"twist right": stopValues["yaw"] + (maximasValues["twist right"] - stopValues["yaw"])/5
}

stopPosition = Twist()
stopPosition.linear.x = stopValues["transversal"]
stopPosition.angular.z = stopValues["yaw"]

pub = rospy.Publisher(topicName, Twist, queue_size = 1)


def writeOnTopic(
	transversal = stopValues["transversal"],
	yaw = stopValues["yaw"],
	pubToWrite = pub,
	stop = False):
	if stop:
		pubToWrite.publish(stopPosition)
	else:
		twist = Twist()
		twist.linear.x = transversal
		twist.angular.z = yaw
		pubToWrite.publish(twist)


if __name__ == '__main__':
	pass
