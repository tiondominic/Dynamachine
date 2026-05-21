import NFA
import draw_nfa

a = NFA.NFA("a|a*")

print("Accepted" if a.validate_string("ab") else "Rejected")

draw_nfa.draw_nfa(a.start_state)
