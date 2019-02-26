#!/usr/bin/env python3
# -*-coding:utf-8 -*


from Config.topic_hexapod import topicName
from Config.config_hexapod import scaleChangeTH as scaleChange
import rospy
from geometry_msgs.msg import Twist


def callback(data):
	print(scaleChange(data))
	

if __name__ == '__main__':
	print("Connection...")
	rospy.init_node('GillouQuiEcoute', anonymous=False)
	print("Connected !")
	rospy.Subscriber(topicName, Twist, callback)
	rospy.spin()
