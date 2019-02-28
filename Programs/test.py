#!/usr/bin/env python3
# -*-coding:utf-8 -*


import rospy
from std_msgs.msg import String


if __name__ == '__main__':
	try:
		print("Connection...")
		rospy.init_node('Talker', anonymous=False)
		print("Connected !")
		pub = rospy.Publisher('hexapod/serial_command', String, queue_size = 5)


		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			pub.publish(input())
			rate.sleep()
	except rospy.ROSInterruptException:
		pass
