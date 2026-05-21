import NFA
import draw_nfa

a = NFA.NFA(input("Enter regex: "))
draw_nfa.draw_nfa(a.start_state)
