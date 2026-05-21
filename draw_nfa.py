import graphviz
from NFA import State

import graphviz

def draw_nfa(start_state: State):
    dot = graphviz.Digraph('NFA', comment='NFA', format='png')
    visited = set()

    def traverse(state: State):
        if state in visited:
            return

        visited.add(state)
        state_id = str(state)

        if state.end_state:
            dot.node(state_id, state_id, shape='doublecircle')
        else:
            dot.node(state_id, state_id, shape='circle')

        for input_char, next_states in state.transitions.items():
            for next_state in next_states:
                next_state_id = str(next_state)
                dot.edge(state_id, next_state_id, label=str(input_char))
                traverse(next_state)

    traverse(start_state)

    dot.node('start', shape='point')
    dot.edge('start', str(start_state))

    dot.view(filename='nfa_output', cleanup=True)