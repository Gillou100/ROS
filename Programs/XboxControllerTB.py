#!/usr/bin/env python3
# -*-coding:utf-8 -*


from Useful.XboxOneController import XboxOneController as Controller
from Useful.useful import control
from Config.topic_turtle_bot import maximasValues, stopValues, minValues, writeOnTopic
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
					transversal = control(controller["SL"]["V"], minValues["forward"], minValues["backward"], stopValues["transversal"]),
					yaw = control(controller["SR"]["H"], minValues["twist left"], minValues["twist right"], stopValues["yaw"])
				)
			rate.sleep()
	finally:
		controller.stop()
