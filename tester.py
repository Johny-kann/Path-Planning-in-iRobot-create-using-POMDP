__author__ = 'Johny Kannan'

import CreateRobot.myRobot as model
import CreateRobot as funcs
import numpy as np


state = [model.State(None, None, None, None) for i in range(0, 10)]

graph = model.PomdpGraph(10, 8)

graph.make_block(2, 1)
graph.make_block(2, 2)
graph.make_block(2, 3)
graph.make_block(2, 4)
graph.make_block(2, 5)
graph.make_block(2, 6)
graph.make_block(2, 7)

graph.make_block(4, 0)
graph.make_block(4, 1)
graph.make_block(4, 2)
graph.make_block(4, 3)
graph.make_block(4, 4)
graph.make_block(4, 5)

graph.re_graph()


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
graph.get_state(0, 2).belief = 200
graph.normalize()

funcs.print_graph_belief(graph)

graph.get_state(3, 3).set_as_destination(100)
funcs.print_pomdp_utility(graph)

graph.find_optimal_pomdp()

funcs.print_pomdp_utility(graph)

funcs.print_utility(graph)


# # action = {'Left': True, 'Right': False, 'Up': False, 'Down': False}
# action = get_max_state().utility[1]
# evidence = {'Left': 0.0, 'Right': 0.0, 'Up': 0.0,'Down': 0.0, 'Center': 1.0}
# graph.update_beliefs(action)
# #graph.normalize()
# graph.update_evidence(evidence)
# graph.normalize()
# funcs.print_graph_belief(graph)



