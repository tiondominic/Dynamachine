import NFA
import DFA
import draw_nfa

regex = "abcdefghijklmnopqrst"
a = NFA.NFA(regex)
b = DFA.DFA(a)

# print(f"Testing regex: {regex}")
# while True:
#     b = input("Input Test String (type exit): ")
#     if b.lower() == "exit":
#         break
#
#     print("Accepted" if a.validate_string(b) else "Rejected")

b.minimize_nfa()

# draw_nfa.draw_nfa(a.start_state)


# TODO:
# add transition table
# add all symbols from regex
# add 