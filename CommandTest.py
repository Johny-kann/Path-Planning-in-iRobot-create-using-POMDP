__author__ = 'Johny kann'

import create
import CreateRobot.myRobot as myRobot
import threading as thread
import CreateRobot.RobotFunctions as funcs
import time, sys, os


robot = create.Create('COM3')
robot.toSafeMode()

robo = myRobot.Robot(robot)
robo.vector['x'] = 0.0
robo.vector['y'] = -1.0

robo.start_sensing()

for i in  range(3):
    robo.go_down()

robo.robot_stop()

