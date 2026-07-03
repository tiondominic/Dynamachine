class State():
    def __init__(self, state_name="", end_state=False):
        self.initial_state = False
        self.transitions = {}
        self.state_name = state_name
        self.end_state = end_state


    def add_transition(self, at, state):
        pass

    def __repr__(self):
        return f"{self.state_name}"
