import create
import pygame, time, sys
from pygame.locals import *
import CreateRobot as robFuncs

robot = create.Create('COM3')

robot.toSafeMode()

# DriveDirect(robot,-50,50,5)

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Keyboard Test')

while True:

    for event in pygame.event.get():
        if event.type == KEYUP:
            robot.stop()
            robot.toSafeMode()

        elif event.type == KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_UP] != 0:
                if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
                    robot.driveDirect(20, 50)

                elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
                    robot.driveDirect(50, 20)
                else:
                    robot.driveDirect(100, 100)
            elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
                if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
                    robot.driveDirect(-20, -50)

                elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
                    robot.driveDirect(-50, -20)
                else:
                    robot.driveDirect(-100, -100)
            elif pygame.key.get_pressed()[pygame.K_LEFT] != 0:
                robot.driveDirect(-50, 50)
            elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
                robot.driveDirect(50, -50)

            elif pygame.key.get_pressed()[pygame.K_s] != 0:
                print(robFuncs.get_analog_sensor(robot))
                print(robFuncs.get_digital_sensor(robot))

        elif event.type == pygame.QUIT:
            robot.toSafeMode()
            sys.exit(0)

        time.sleep(0.2)

