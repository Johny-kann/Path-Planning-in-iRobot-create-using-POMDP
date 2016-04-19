__author__ = 'Johny Kannan'


class State:

    def __init__(self, left_state, right_state, top_state, bottom_state, x = None, y = None):
        self.belief = 1.0
        self.policy = {'stay': 0, 'front': 1, 'left': 0, 'right': 0, 'back': 0}
        self.left_state = left_state
        self.right_state = right_state
        self.top_state = top_state
        self.bottom_state = bottom_state
        self.pos = {'x': x, 'y': y}
        self.block = False


    def set_nearby_states(self, left_state, right_state, top_state, bottom_state):
        self.left_state = left_state
        self.right_state = right_state
        self.top_state = top_state
        self.bottom_state = bottom_state

    def set_block(self):
        self.block = True
        self.belief = 0.0
        self.set_nearby_states(None, None, None, None)


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

    def make_block(self, x, y):
        self.get_state(x, y).set_block()

        if x > 0:
            self.get_state(x-1, y).right_state = None
        if x < self.dimension['length']-1:
            self.get_state(x+1, y).left_state = None
        if y > 0:
            self.get_state(x, y-1).bottom_state = None
        if y < self.dimension['breadth']-1:
            self.get_state(x, y+1).top_state = None

    def normalize(self):
        vec = [self.states[i].belief for i in range(0, len(self.states))]
        addition = sum(vec)
        vec[:] = [x/addition for x in vec]
        for i in range(0, len(self.states)):
            self.states[i].belief = round(vec[i], 4)

    def __left_action_possible(self, state):
        '''
        Possibility to reach this state through by moving left P(S'|action = 'Front')
        :param state:
        :return:
        '''
        if state.block is False and state.right_state is not None:
            return True
        else:
            return False

    def __right_action_possible(self, state):
        '''
        Possibility to reach this state through by moving right P(S'|action = 'Right')
        :param state:
        :return:
        '''
        if state.block is False and state.left_state is not None:
            return True
        else:
            return False

    def __top_action_possible(self, state):
        '''
        Possibility to reach this state through by moving top P(S'|action = 'Top')
        :param state:
        :return:
        '''
        if state.block is False and state.bottom_state is not None:
            return True
        else:
            return False

    def __bottom_action_possible(self, state):
        '''
        Possibility to reach this state through by moving top P(S'|action = 'Bottom')
        :param state:
        :return:
        '''
        if state.block is False and state.top_state is not None:
            return True
        else:
            return False

    def update_beliefs(self, action):
        '''
        Updates the beliefs of the states based on the action given
        :param action: is dictionary of sample {'Left':true,'Right':false, 'Up':false,'Down':false} in terms of the POMDP graph
        '''
        for i in range(0, len(self.states)):
            if action['Left'] and self.__left_action_possible(self.states[i]):
                self.states[i].belief += 10*self.states[i].right_state.belief
            elif action['Right'] and self.__right_action_possible(self.states[i]):
                self.states[i].belief += 10*self.states[i].left_state.belief
            elif action['Up'] and self.__top_action_possible(self.states[i]):
                self.states[i].belief += 10*self.states[i].bottom_state.belief
            elif action['Down'] and self.__bottom_action_possible(self.states[i]):
                self.states[i].belief += 10*self.states[i].top_state.belief

    def update_evidence(self, evidence):
        '''
        Updates the evidence with the belief state
        :param evidence: dictionary of sample {'Left':1,'Right':1,'Up':0,'Down':0,'Center':0}
        :return:
        '''
        for state in self.states:
            if state.block is False:
                if state.left_state is None:
                    state.belief += (evidence['Left']*.7 + evidence['Right']*0 + evidence['Up']*.1 + evidence['Down']*.1 + evidence['Center']*.1)*5
                if state.right_state is None:
                    state.belief += (evidence['Left']*0 + evidence['Right']*0.7 + evidence['Up']*.1 + evidence['Down']*.1 + evidence['Center']*.1)*5
                if state.top_state is None:
                    state.belief += (evidence['Left']*.1 + evidence['Right']*0.1 + evidence['Up']*.8 + evidence['Down']*0 + evidence['Center']*0.0)*5
                if state.bottom_state is None:
                    state.belief += (evidence['Left']*.1 + evidence['Right']*0.1 + evidence['Up']*0 + evidence['Down']*.8 + evidence['Center']*0.0)*5
                if state.left_state is not None and state.right_state is not None and state.top_state is not None and state.bottom_state is not None:
                    state.belief += (evidence['Left']*.15 + evidence['Right']*.15 + evidence['Up']*.15 + evidence['Down']*.15 + evidence['Center']*.6)*5

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
                    if self.get_state(x-1, y).block is not True:
                        value.left_state = self.get_state(x-1, y)
                if x < self.dimension['length']-1:
                    if self.get_state(x+1, y).block is not True:
                        value.right_state = self.get_state(x+1, y)
                if y > 0:
                    if self.get_state(x, y-1).block is not True:
                        value.top_state = self.get_state(x, y-1)
                if y < self.dimension['breadth']-1:
                    if self.get_state(x, y+1).block is not True:
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
        self.direction = {'x': 1.0, 'y': 0.0}