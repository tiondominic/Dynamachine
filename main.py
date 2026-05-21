import NFA
import draw_nfa

a = NFA.NFA("b|a*")

print("Accepted" if a.validate_string("a") else "Rejected")

draw_nfa.draw_nfa(a.start_state)
