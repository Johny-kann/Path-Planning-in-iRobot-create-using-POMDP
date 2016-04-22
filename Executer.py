__author__ = 'Johny Kannan'

import CreateRobot.myRobot as model
import CreateRobot as funcs
import create

graph = model.PomdpGraph(6, 2)

robot = create.Create('COM3')
robot.toSafeMode()

robo = model.Robot(robot)

graph.make_block(1, 0)
# graph.make_block(2, 2)
# graph.make_block(2, 3)
# graph.make_block(2, 4)
# graph.make_block(2, 5)
# graph.make_block(2, 6)
# graph.make_block(2, 7)
#
# graph.make_block(4, 0)
# graph.make_block(4, 1)
# graph.make_block(4, 2)
# graph.make_block(4, 3)
# graph.make_block(4, 4)
# graph.make_block(4, 5)

graph.re_graph()

graph.get_state(3, 0).belief = 200

robo.vector['x'] = 0.0
robo.vector['y'] = 1.0

graph.get_state(0, 0).set_as_destination(100)
graph.reward_state = graph.get_state(0, 0)

for y in range(0, graph.dimension['breadth']):
    for x in range(0, graph.dimension['length']):
        if graph.get_state(x,y).left_state is None:
            print('L', end='')
        if graph.get_state(x,y).top_state is None:
            print('T', end='')
        if graph.get_state(x,y).right_state is None:
            print('R', end='')
        if graph.get_state(x,y).bottom_state is None:
            print('D', end='')
        print('\t', end='')
    print()

graph.normalize()

graph.find_utility_optimal_MDP()
funcs.print_utility(graph)

robo.start_sensing()

for i in range(10):
    print('===========================================', end='\n')
    max_state = graph.get_max_state()
    if max_state.utility[1] is 'Stay':
        break
    action = max_state.utility[1]
    print(max_state.pos, max_state.utility)

    robo.execute_action(action)
    evidence = robo.evidence
    print(evidence)
    graph.update_beliefs(action)
    graph.update_evidence(evidence)
    graph.normalize()
    funcs.print_graph_belief(graph)
    print('===========================================', end='\n\n')

robo.robot_stop()



