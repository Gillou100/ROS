#!/usr/bin/env python3
# -*-coding:utf-8 -*


from geometry_msgs.msg import Twist
import rospy


topicName = 'hexapod/cmd_vel'

maximasValues = {
	"forward": 255,
	"backward": 0,
	"left": 0,
	"right": 255,
	"up": 255,
	"down": 0,
	"lean left": 0,
	"lean right": 255,
	"lean forward": 255,
	"lean backward": 0,
	"twist left": 0,
	"twist right": 255
}
stopValues = {
	"transversal": int((maximasValues["forward"] + maximasValues["backward"])/2),
	"lateral": int((maximasValues["left"] + maximasValues["right"])/2),
	"height": int((maximasValues["up"] + maximasValues["down"])/2),
	"twist transversal": int((maximasValues["lean left"] + maximasValues["lean right"])/2),
	"twist lateral": int((maximasValues["lean forward"] + maximasValues["lean backward"])/2),
	"twist height": int((maximasValues["twist left"] + maximasValues["twist right"])/2),
}
centralValues = {
	"forward": stopValues["transversal"] + (maximasValues["forward"] - stopValues["transversal"])/5,
	"backward": stopValues["transversal"] + (maximasValues["backward"] - stopValues["transversal"])/5,
	"left": stopValues["lateral"] + (maximasValues["left"] - stopValues["lateral"])/5,
	"right":  stopValues["lateral"] + (maximasValues["right"] - stopValues["lateral"])/5,
	"up": stopValues["height"] + (maximasValues["up"] - stopValues["height"])/5,
	"down": stopValues["height"] + (maximasValues["down"] - stopValues["height"])/5,
	"lean left": stopValues["twist transversal"] + (maximasValues["lean left"] - stopValues["twist transversal"])/5,
	"lean right": stopValues["twist transversal"] + (maximasValues["lean right"] - stopValues["twist transversal"])/5,
	"lean forward": stopValues["twist lateral"] + (maximasValues["lean forward"] - stopValues["twist lateral"])/5,
	"lean backward": stopValues["twist lateral"] + (maximasValues["lean backward"] - stopValues["twist lateral"])/5,
	"twist left": stopValues["twist height"] + (maximasValues["twist left"] - stopValues["twist height"])/5,
	"twist right": stopValues["twist height"] + (maximasValues["twist right"] - stopValues["twist height"])/5
}

stopPosition = Twist()
stopPosition.linear.x = stopValues["transversal"]
stopPosition.linear.y = stopValues["lateral"]
stopPosition.linear.z = stopValues["height"]
stopPosition.angular.x = stopValues["twist transversal"]
stopPosition.angular.y = stopValues["twist lateral"]
stopPosition.angular.z = stopValues["twist height"]

pub = rospy.Publisher(topicName, Twist, queue_size = 1)


def writeOnTopic(
	transversal = stopValues["transversal"],
	lateral = stopValues["lateral"],
	height = stopValues["height"],
	twistTransversal = stopValues["twist transversal"],
	twistLateral = stopValues["twist lateral"],
	twistHeight = stopValues["twist height"],
	pubToWrite = pub,
	stop = False):
	if stop:
		pubToWrite.publish(stopPosition)
	else:
		twist = Twist()
		twist.linear.x = transversal
		twist.linear.y = lateral
		twist.linear.z = height
		twist.angular.x = twistTransversal
		twist.angular.y = twistLateral
		twist.angular.z = twistHeight
		pubToWrite.publish(twist)

if __name__ == '__main__':
	pass
