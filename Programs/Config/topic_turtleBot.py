#!/usr/bin/env python3
# -*-coding:utf-8 -*


from geometry_msgs.msg import Twist


topicName = '/cmd_vel'


topicMaximas = {
	"TX" : {
		"forward" : 0.22,
		"backward" : -0.22
	},
	"RZ" : {
		"twist left" : 2.84,
		"twist right" : -2.84
	}
}
middleValues = {
	"TX": (topicMaximas["TX"]["forward"] + topicMaximas["TX"]["backward"])/2,
	"RZ": (topicMaximas["RZ"]["twist left"] + topicMaximas["RZ"]["twist right"])/2
}
centralValues = {
	"TX": [middleValues["TX"] + (topicMaximas["TX"]["forward"] - middleValues["TX"])/5, middleValues["TX"] + (topicMaximas["TX"]["backward"] - middleValues["TX"])/5],
	"RZ": [middleValues["RZ"] + (topicMaximas["RZ"]["twist left"] - middleValues["RZ"])/5, middleValues["RZ"] + (topicMaximas["RZ"]["twist right"] - middleValues["RZ"])/5]
}

stopPosition = Twist()
stopPosition.linear.x = middleValues["TX"]
stopPosition.linear.y = 0
stopPosition.linear.z = 0
stopPosition.angular.x = 0
stopPosition.angular.y = 0
stopPosition.angular.z = middleValues["RZ"]


if __name__ == '__main__':
	pass
