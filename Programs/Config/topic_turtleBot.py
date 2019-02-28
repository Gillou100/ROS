#!/usr/bin/env python3
# -*-coding:utf-8 -*


from geometry_msgs.msg import Twist
import rospy


topicName = '/cmd_vel'

maximasValues = {
	"forward" : 0.22,
	"backward" : -0.22,
	"twist left" : 2.84,
	"twist right" : -2.84
}
stopValues = {
	"transversal": int((maximasValues["forward"] + maximasValues["backward"])/2),
	"twist height": int((maximasValues["twist left"] + maximasValues["twist right"])/2),
}
centralValues = {
	"forward": stopValues["transversal"] + (maximasValues["forward"] - stopValues["transversal"])/5,
	"backward": stopValues["transversal"] + (maximasValues["backward"] - stopValues["transversal"])/5,
	"twist left": stopValues["twist height"] + (maximasValues["twist left"] - stopValues["twist height"])/5,
	"twist right": stopValues["twist height"] + (maximasValues["twist right"] - stopValues["twist height"])/5
}

stopPosition = Twist()
stopPosition.linear.x = stopValues["transversal"]
stopPosition.angular.z = stopValues["twist height"]

pub = rospy.Publisher(topicName, Twist, queue_size = 1)


def writeOnTopic(
	transversal = stopValues["transversal"],
	twistHeight = stopValues["twist height"],
	pubToWrite = pub,
	stop = False):
	if stop:
		pubToWrite.publish(stopPosition)
	else:
		twist = Twist()
		twist.linear.x = transversal
		twist.angular.z = twistHeight
		pubToWrite.publish(twist)


if __name__ == '__main__':
	pass
