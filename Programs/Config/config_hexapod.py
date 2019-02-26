#!/usr/bin/env python3
# -*-coding:utf-8 -*


from geometry_msgs.msg import Twist
from Config.topic_hexapod import topicMaximas
from Useful.useful import scaleChange


hexapodMaximas = {
	"TX" : {
		"m" : 0,
		"M" : 256
	},
	"TY" : {
		"m" : 0,
		"M" : 256
	},
	"TZ" : {
		"m" : 0,
		"M" : 256
	},
	"RX" : {
		"m" : 0,
		"M" : 256
	},
	"RY" : {
		"m" : 0,
		"M" : 256
	},
	"RZ" : {
		"m" : 0,
		"M" : 256
	}
}


def scaleChangeTH(v):
	newV = Twist()

	newV.linear.x = scaleChange(v.linear.x, topicMaximas["TX"]["m"], topicMaximas["TX"]["M"], hexapodMaximas["TX"]["m"], hexapodMaximas["TX"]["M"])
	newV.linear.y = scaleChange(v.linear.y, topicMaximas["TY"]["m"], topicMaximas["TY"]["M"], hexapodMaximas["TY"]["m"], hexapodMaximas["TY"]["M"])
	newV.linear.z = scaleChange(v.linear.z, topicMaximas["TZ"]["m"], topicMaximas["TZ"]["M"], hexapodMaximas["TZ"]["m"], hexapodMaximas["TZ"]["M"])
	newV.angular.x = scaleChange(v.angular.x, topicMaximas["RX"]["m"], topicMaximas["RX"]["M"], hexapodMaximas["RX"]["m"], hexapodMaximas["RX"]["M"])
	newV.angular.y = scaleChange(v.angular.y, topicMaximas["RY"]["m"], topicMaximas["RY"]["M"], hexapodMaximas["RY"]["m"], hexapodMaximas["RY"]["M"])
	newV.angular.z = scaleChange(v.angular.z, topicMaximas["RZ"]["m"], topicMaximas["RZ"]["M"], hexapodMaximas["RZ"]["m"], hexapodMaximas["RZ"]["M"])

	return newV


if __name__ == '__main__':
	pass
