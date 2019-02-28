#!/usr/bin/env python3
# -*-coding:utf-8 -*


from geometry_msgs.msg import Twist


topicName = 'hexapod/cmd_vel'


topicMaximas = {
	"TX" : {
		"forward" : 255,
		"backward" : 0
	},
	"TY" : {
		"left" : 0,
		"right" : 255
	},
	"TZ" : {
		"up" : 255,
		"down" : 0
	},
	"RX" : {
		"lean left" : 0,
		"lean right" : 255
	},
	"RY" : {
		"lean forward" : 255,
		"lean backward" : 0
	},
	"RZ" : {
		"twist left" : 0,
		"twist right" : 255
	}
}
middleValues = {
	"TX": (topicMaximas["TX"]["forward"] + topicMaximas["TX"]["backward"])/2,
	"TY": (topicMaximas["TY"]["left"] + topicMaximas["TY"]["right"])/2,
	"TZ": (topicMaximas["TZ"]["up"] + topicMaximas["TZ"]["down"])/2,
	"RX": (topicMaximas["RX"]["lean left"] + topicMaximas["RX"]["lean right"])/2,
	"RY": (topicMaximas["RY"]["lean forward"] + topicMaximas["RY"]["lean backward"])/2,
	"RZ": (topicMaximas["RZ"]["twist left"] + topicMaximas["RZ"]["twist right"])/2
}
centralValues = {
	"TX": [middleValues["TX"] + (topicMaximas["TX"]["forward"] - middleValues["TX"])/5, middleValues["TX"] + (topicMaximas["TX"]["backward"] - middleValues["TX"])/5],
	"TY": [middleValues["TY"] + (topicMaximas["TY"]["left"] - middleValues["TY"])/5, middleValues["TY"] + (topicMaximas["TY"]["right"] - middleValues["TY"])/5],
	"TZ": [middleValues["TZ"] + (topicMaximas["TZ"]["up"] - middleValues["TZ"])/5, middleValues["TZ"] + (topicMaximas["TZ"]["down"] - middleValues["TZ"])/5],
	"RX": [middleValues["RX"] + (topicMaximas["RX"]["lean left"] - middleValues["RX"])/5, middleValues["RX"] + (topicMaximas["RX"]["lean right"] - middleValues["RX"])/5],
	"RY": [middleValues["RY"] + (topicMaximas["RY"]["lean forward"] - middleValues["RY"])/5, middleValues["RY"] + (topicMaximas["RY"]["lean backward"] - middleValues["RY"])/5],
	"RZ": [middleValues["RZ"] + (topicMaximas["RZ"]["twist left"] - middleValues["RZ"])/5, middleValues["RZ"] + (topicMaximas["RZ"]["twist right"] - middleValues["RZ"])/5]
}

stopPosition = Twist()
stopPosition.linear.x = middleValues["TX"]
stopPosition.linear.y = middleValues["TY"]
stopPosition.linear.z = middleValues["TZ"]
stopPosition.angular.x = middleValues["RX"]
stopPosition.angular.y = middleValues["RY"]
stopPosition.angular.z = middleValues["RZ"]

if __name__ == '__main__':
	pass
