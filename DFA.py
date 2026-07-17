import State
import NFA


class DFAState(State.State):
    def add_transition(self, at, state):
        self.transitions[at] = state

class DFA:
    def __init__(self, nfa, symbols):
        self.nfa = nfa
        self.dfa = None
        self.transition_table = set()
        self.symbols = symbols
        # {q0: {q1, q2, q3, q043}, q1: {qDead} etc..

        pass


    def create_dfa(self):

        pass
    def minimize_nfa(self):
        pass








