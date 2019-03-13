#!/usr/bin/env python3
# -*-coding:utf-8 -*


from Useful.XboxOneController import XboxOneController as Controller
from Useful.useful import control
from Config.topic_virtual_turtle import maximasValues, stopValues, minValues, writeOnTopic
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
			elif controller["U"]:
				writeOnTopic(
					transversal = maximasValues["forward"],
					yaw = stopValues["yaw"]
				)
			elif controller["D"]:
				writeOnTopic(
					transversal = maximasValues["backward"],
					yaw = stopValues["yaw"]
				)
			elif controller["L"]:
				writeOnTopic(
					transversal = stopValues["transversal"],
					yaw = maximasValues["twist left"]
				)
			elif controller["R"]:
				writeOnTopic(
					transversal = stopValues["transversal"],
					yaw = maximasValues["twist right"]
				)
                        else:
                                writeOnTopic(
                                        transversal = control(controller["SL"]["V"], minValues["forward"$
                                        yaw = control(controller["SR"]["H"], minValues["twist left"], mi$
                                )
			rate.sleep()
	finally:
		controller.stop()
