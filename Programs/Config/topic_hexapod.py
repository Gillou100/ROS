#!/usr/bin/env python3
# -*-coding:utf-8 -*


from geometry_msgs.msg import Twist


#topicName = 'hexapod/cmd_vel'
topicName = 'hexapod/serial_command'


topicMaximas = {
	"TX" : {
		"m" : -100,
		"M" : 100
	},
	"TY" : {
		"m" : -100,
		"M" : 100
	},
	"TZ" : {
		"m" : 0,
		"M" : 0
	},
	"RX" : {
		"m" : 0,
		"M" : 0
	},
	"RY" : {
		"m" : -100,
		"M" : 100
	},
	"RZ" : {
		"m" : -100,
		"M" : 100
	}
}
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

stopPosition = Twist()
stopPosition.linear.x = middleValues["TX"]
stopPosition.linear.y = middleValues["TY"]
stopPosition.linear.z = middleValues["TZ"]
stopPosition.angular.x = middleValues["RX"]
stopPosition.angular.y = middleValues["RY"]
stopPosition.angular.z = middleValues["RZ"]

if __name__ == '__main__':
	pass
