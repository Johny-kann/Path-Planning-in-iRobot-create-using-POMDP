__author__ = 'Johny Kannan'

import CreateRobot.myRobot as model
import numpy as np


state = [ model.State(None, None, None, None) for i in range(0, 10) ]

# for i in range(0, 5):
#     if i is not 0:
#         state[i].left_state = state[i-1]
#     if i is not 4:
#         state[i].right_state = state[i+1]
#
#     state[i].bottom_state = state[i+5]
#     state[i].pos = {'x': i, 'y': 0}
#
#
# for i in range(5, 10):
#     if i is not 5:
#         state[i].left_state = state[i-1]
#     if i is not 9:
#         state[i].right_state = state[i+1]
#
#     state[i].top_state = state[i-5]
#     state[i].pos = {'x': i-5, 'y': 1}

graph = model.PomdpGraph(4,3)

graph.re_graph()

graph.normalize()

for states in graph.states:
    if states.left_state is None and states.top_state is None:
        print(' left-up ', states.pos)
    elif states.right_state is None and states.top_state is None:
        print(" right Up", states.pos)
    elif states.left_state is None and states.bottom_state is None:
        print(' left-down ', states.pos)
    elif states.right_state is None and states.bottom_state is None:
        print(' right-down ', states.pos)
    elif states.top_state is None:
        print(' Up ', states.pos)
    elif states.bottom_state is None:
        print(' Bottom ', states.pos)
    else:
        print(' Center ', states.pos)

# vec = [1] * len(graph.states)
# vec[3] *= 100
x = 2; y = 2

graph.states[4*y + x].belief *= 10


graph.normalize()

# for i in range(len(graph.states)):
#     graph.states[i].belief *= vec[i]

array = np.array([graph.states[i].belief for i in range(len(graph.states))]).reshape(graph.dimension['breadth'], graph.dimension['length'])

print(array)
