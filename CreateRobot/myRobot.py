__author__ = 'Johny Kannan'


class State:

    def __init__(self, left_state, right_state, top_state, bottom_state, x = None, y = None):
        self.utility = 1.0
        self.policy = {'stay': 0, 'front': 1, 'left': 0, 'right': 0, 'back': 0}
        self.left_state = left_state
        self.right_state = right_state
        self.top_state = top_state
        self.bottom_state = bottom_state
        self.pos = {'x': x, 'y': y}

    def set_nearby_states(self, left_state, right_state, top_state, bottom_state):
        self.left_state = left_state
        self.right_state = right_state
        self.top_state = top_state
        self.bottom_state = bottom_state


class PomdpGraph:

    def __init__(self, length, breadth):
        self.dimension = {'length': length, 'breadth': breadth}
#        self.states = [0]*length*breadth
        self.states = [State(None, None, None, None) for i in range(0, length*breadth)]

    def set_states_list(self, states):
        self.states = states

    def get_state(self, x, y):
        return self.states[self.dimension['length']*y+x]

    def set_state(self, x, y, value):
        self.states[self.dimension['length']*y+x] = value

    def normalize(self):
        vec = [self.states[i].utility for i in range(0, len(self.states))]
        addition = sum(vec)
        vec[:] = [x/addition for x in vec]
        for i in range(0, len(self.states)):
            self.states[i].utility = vec[i]

    def insert(self, x, y, value):
        if x >= self.dimension['x'] or y >= self.dimension['y']:
            return False
        else:
            if x > 0:
                value.left_state = self.get_state(x-1, y)
            if x < self.dimension['breadth']-1:
                value.right_state = self.get_state(x+1, y)
            if y > 0:
                value.top_state = self.get_state(x, y-1)
            if y < self.dimension['length']-1:
                value.bottom_state = self.get_state(x, y+1)

            return True

    def re_graph(self):
        length = self.dimension['length']
        breadth = self.dimension['breadth']

        for x in range(0, length):
            for y in range(0, breadth):
                value = self.get_state(x, y)
                value.pos['x'] = x
                value.pos['y'] = y
                if x > 0:
                    value.left_state = self.get_state(x-1, y)
                if x < self.dimension['length']-1:
                    value.right_state = self.get_state(x+1, y)
                if y > 0:
                    value.top_state = self.get_state(x, y-1)
                if y < self.dimension['breadth']-1:
                    value.bottom_state = self.get_state(x, y+1)


class Robot:
    """
    The class I use to control Robot.
    It will record the previous states, sensor values etc
    """

    def __init__(self, create):
        self.robot = create
        self.vector = {'x': 1.0, 'y': 0.0}
        self.analog_sensor = dict()
        self.digit_sensor = dict()