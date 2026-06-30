import State
import NFA


class DFAState(State.State):
    def add_transition(self, at, state):
        self.transitions[at] = state

class DFA:
    def __init__(self, nfa):
        self.nfa = nfa
        self.dfa = None

        pass


    def create_dfa(self):

        pass
    def minimize_nfa(self):
        transitions = {}
        self.dfa = None
        print(f"Printing transitions for {self.nfa.start_state}")
        temp = self.nfa.start_state.transitions
        for i in temp:
            for j in temp[i]:
                print(f"{self.nfa.start_state} -{i}> {j}")

        pass

