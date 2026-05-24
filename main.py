import NFA
import draw_nfa

regex = "((a|b)c)*"
a = NFA.NFA(regex)

print(f"Testing regex: {regex}")
while True:
    b = input("Input Test String (type exit): ")
    if b.lower() == "exit":
        break

    print("Accepted" if a.validate_string(b) else "Rejected")


draw_nfa.draw_nfa(a.start_state)
