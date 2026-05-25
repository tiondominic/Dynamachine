import State

class DFAState(State.State):
    def add_transition(self, at, state):
        self.transitions[at] = state

class DFA:
    def __init__(self):
        pass

