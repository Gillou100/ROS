#!/usr/bin/env python3
# -*-coding:utf-8 -*


from Useful.XboxOneController import XboxOneController as Controller
from Useful.useful import control
from Config.topic_turtleBot import maximasValues, stopValues, centralValues, writeOnTopic
import rospy


if __name__ == '__main__':
	try:
		print("Connection...")
		rospy.init_node('XboxOneController', anonymous=False)
		print("Connected !")
		writeOnTopic(stop = True)


		controller = Controller(
			SLU = maximasValues["forward"],
			SLD = maximasValues["backward"],
			SRL = maximasValues["twist left"],
			SRR = maximasValues["twist right"]
		)
		controller.start()

		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			if controller["A"]:
				writeOnTopic(stop = True)
			else:
				writeOnTopic(
					transversal = control(controller["SL"]["V"], centralValues["forward"], centralValues["backward"], stopValues["transversal"]),
					twistHeight = control(controller["SR"]["H"], centralValues["twist left"], centralValues["twist right"], stopValues["yaw"])
				)
			rate.sleep()
	finally:
		controller.stop()
