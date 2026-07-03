import NFA
import DFA
import draw_nfa

regex = "a|b"
a = NFA.NFA(regex)
a.print_symbols()
print("printing table")
a.print_table()
draw_nfa.draw_nfa(a.start_state)
b = DFA.DFA(a, a.symbols)



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