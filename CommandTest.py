__author__ = 'Johny kann'

import create
import CreateRobot.myRobot as myRobot
import threading as thread
import CreateRobot.RobotFunctions as funcs
import time, sys, os


robot = create.Create('COM3')
robot.toSafeMode()

robo = myRobot.Robot(robot)

lock = thread.RLock()

robo_active = True

def stop_robot():
    robot.stop()

def sensor_values():
    global robo_active
    while robo_active:
        asen = funcs.get_analog_sensor(robot)
        dsen = funcs.get_digital_sensor(robot)
        if (dsen['bump_and_sensors']['BUMP_LEFT'] is 1):
            stop_robot()
            robo.bump_left_remedy()

        if (dsen['bump_and_sensors']['BUMP_RIGHT'] is 1):
            stop_robot()
            robo.bump_right_remedy()

        # print(asen, dsen, sep='\n')
        time.sleep(0.3)

def print_thread():
    global robo_active
    while robo_active:
        print('I am in thread')
        time.sleep(.5)

k = 5
robo_active = True
t = thread.Timer(.1, sensor_values)
t.start()
robo.vector['x'] = 0.0
robo.vector['y'] = 1.0
robo.go_right()
robo.go_left()

robo_active = False
