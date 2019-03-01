#!/usr/bin/env python3
# -*-coding:utf-8 -*


import rospy,time,serial
from geometry_msgs.msg import Twist
from Config._serial_frame import serial_frame
from Config.config_hexapod import scaleChangeTH as scaleChange
from Config.topic_hexapod import topicName


port = "/dev/ttyUSB0"
baud = 38400
ser = serial.Serial(port, baud, timeout=1)

serial_frame = serial_frame()


def checksum(serial_frame):
	sum = serial_frame.right_v_byte + serial_frame.right_h_byte + serial_frame.left_v_byte + serial_frame.left_h_byte + serial_frame.button_byte
	return(255-(sum % 256))


def callback(data):
	serial_frame.header_byte = 255
	serial_frame.right_v_byte = int(data.angular.y)
	serial_frame.right_h_byte = int(data.angular.z)
	serial_frame.left_v_byte = int(data.linear.x)
	serial_frame.left_h_byte = int(data.linear.y)
	serial_frame.button_byte = 16
	serial_frame.end_byte = 0
	serial_frame.checksum_byte = checksum(serial_frame)


def arbotix_node():
	print("Connection...")
	rospy.init_node('Hexapod', anonymous=False)
	print("Connected !")
	rospy.Subscriber(topicName, Twist, callback)
	while not rospy.is_shutdown():
		ser.write(bytearray([serial_frame.header_byte,
			serial_frame.right_v_byte, serial_frame.right_h_byte,
			serial_frame.left_v_byte, serial_frame.left_h_byte,
			serial_frame.button_byte, serial_frame.end_byte,
			serial_frame.checksum_byte]))
		time.sleep(0.033)


if __name__ == '__main__':
	try:
		arbotix_node()
	except rospy.ROSInterruptException:
		pass
