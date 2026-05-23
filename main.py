import NFA
import draw_nfa

a = NFA.NFA("(a|b)*c|b*")

print("Accepted" if a.validate_string("aa") else "Rejected")

draw_nfa.draw_nfa(a.start_state)
