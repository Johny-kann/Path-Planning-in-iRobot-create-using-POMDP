__author__ = 'Johny Kann'

import CreateRobot.myRobot as model

def find_bump_value(num):
    """
    Gives you a dictionary of bump sensor for the given input
    :rtype : Returns a dictionary of bump_sensor
    """
    bump_sensors = {'WHEELDROP_CASTER': num[0], 'WHEELDROP_LEFT': num[1], 'WHEELDROP_RIGHT': num[2], 'BUMP_LEFT': num[3],'BUMP_RIGHT': num[4]}
    return bump_sensors

def get_analog_sensor(robot):
    sensor = dict()
    sensor['wall'] = robot.getSensor("WALL_SIGNAL")
    sensor['cliff_left'] = robot.getSensor("CLIFF_LEFT_SIGNAL")
    sensor['cliff_front_left'] = robot.getSensor("CLIFF_FRONT_LEFT_SIGNAL")
    sensor['cliff_front_right'] = robot.getSensor("CLIFF_FRONT_RIGHT_SIGNAL")
    sensor['cliff_right'] = robot.getSensor("CLIFF_RIGHT_SIGNAL")
    sensor['distance'] = robot.getSensor("DISTANCE")
    sensor['angle'] = robot.getSensor("ANGLE")
    sensor['voltage'] = robot.getSensor("VOLTAGE")
    sensor['charge'] = robot.getSensor("CHARGING_STATE")
    sensor['battery_temp'] = robot.getSensor("BATTERY_TEMPERATURE")
    return sensor

def get_digital_sensor(robot):
    sensor = dict()
    sensor['wall'] = robot.getSensor("WALL")
    sensor['bump_and_sensors'] = find_bump_value(robot.getSensor('BUMPS_AND_WHEEL_DROPS'))
    return sensor

def DriveDirect(robot, left_wheel, right_Wheel, time):
    robot.driveDirect(left_wheel, right_Wheel)
    robot.waitTime(time)
    robot.stop()
    return "Done"

def print_graph_belief(graph):
    for y in range(0, graph.dimension['breadth']):
        for x in range(0, graph.dimension['length']):
            print(graph.get_state(x, y).belief, end='\t|')
        print()
    print()