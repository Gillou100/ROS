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
	"transversal": (maximasValues["forward"] + maximasValues["backward"])/2,
	"lateral": (maximasValues["left"] + maximasValues["right"])/2,
	"height": (maximasValues["up"] + maximasValues["down"])/2,
	"roll": (maximasValues["lean left"] + maximasValues["lean right"])/2,
	"pitch": (maximasValues["lean forward"] + maximasValues["lean backward"])/2,
	"yaw": (maximasValues["twist left"] + maximasValues["twist right"])/2,
}
minValues = {
	"forward": stopValues["transversal"] + (maximasValues["forward"] - stopValues["transversal"])/5,
	"backward": stopValues["transversal"] + (maximasValues["backward"] - stopValues["transversal"])/5,
	"left": stopValues["lateral"] + (maximasValues["left"] - stopValues["lateral"])/5,
	"right":  stopValues["lateral"] + (maximasValues["right"] - stopValues["lateral"])/5,
	"up": stopValues["height"] + (maximasValues["up"] - stopValues["height"])/5,
	"down": stopValues["height"] + (maximasValues["down"] - stopValues["height"])/5,
	"lean left": stopValues["roll"] + (maximasValues["lean left"] - stopValues["roll"])/5,
	"lean right": stopValues["roll"] + (maximasValues["lean right"] - stopValues["roll"])/5,
	"lean forward": stopValues["pitch"] + (maximasValues["lean forward"] - stopValues["pitch"])/5,
	"lean backward": stopValues["pitch"] + (maximasValues["lean backward"] - stopValues["pitch"])/5,
	"twist left": stopValues["yaw"] + (maximasValues["twist left"] - stopValues["yaw"])/5,
	"twist right": stopValues["yaw"] + (maximasValues["twist right"] - stopValues["yaw"])/5
}

stopPosition = Twist()
stopPosition.linear.x = stopValues["transversal"]
stopPosition.linear.y = stopValues["lateral"]
stopPosition.linear.z = stopValues["height"]
stopPosition.angular.x = stopValues["roll"]
stopPosition.angular.y = stopValues["pitch"]
stopPosition.angular.z = stopValues["yaw"]

pub = rospy.Publisher(topicName, Twist, queue_size = 1)


def writeOnTopic(
	transversal = stopValues["transversal"],
	lateral = stopValues["lateral"],
	height = stopValues["height"],
	roll = stopValues["roll"],
	pitch = stopValues["pitch"],
	yaw = stopValues["yaw"],
	pubToWrite = pub,
	stop = False):
	if stop:
		pubToWrite.publish(stopPosition)
	else:
		twist = Twist()
		twist.linear.x = transversal
		twist.linear.y = lateral
		twist.linear.z = height
		twist.angular.x = roll
		twist.angular.y = pitch
		twist.angular.z = yaw
		pubToWrite.publish(twist)

if __name__ == '__main__':
	pass
