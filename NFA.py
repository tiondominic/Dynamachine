class State():
    def __init__(self, state_name="", end_state=False):
        self.transitions = {}
        self.state_name = state_name
        self.end_state = end_state


    def _addTransition(self, at, state):
        if at not in self.transitions:
            self.transitions[at] = []

        self.transitions[at].append(state)

    def __repr__(self):
        return f"{self.state_name}"
class Fragment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class NFA():
    def __init__(self, regex):
        self.start_state = State()
        self.NFA = []
        self.end_state = None
        self.regex = regex
        self._regexToNFA(regex)


    def _regexToNFA(self, regex):
        if self.regex == "":
            self.start_state.end_state = True

        elif len(regex) == 1:

            start = State("", False)
            end = State("", True)

            start._addTransition(regex[0], end)
            return Fragment(start, end)
        # else: # Could add for anything else that does not qualify as an NFA
        #     return State() # Finish later

        segs = self.parse_regex(regex)
        nfa_frags = []
        operations = []

        for seg in segs:
            if seg not in ("*", "|", "."):
                frag = self._regexToNFA(seg)
                nfa_frags.append(frag)
            elif seg == "*":
                old_nfa = nfa_frags.pop()

                old_nfa.end.end_state = False
                old_nfa.end._addTransition("$", old_nfa.start)

                new_start = State("", False)
                new_end = State("", True)

                new_start._addTransition("$", old_nfa.start)
                new_start._addTransition("$", new_end)
                old_nfa.end._addTransition("$", new_end)

                nfa_frags.append(Fragment(new_start, new_end))
            elif seg == ".":
                operations.append(".")
                continue
            elif seg == "|":
                operations.append("|")
            make





    def parse_regex(self, regex):
        count = 0
        temp = ""
        segments = []
        operators = []

        for i in range(len(regex)):
            c = regex[i]
            if c == "(":
                count += 1
                if count == 1:
                    continue
            elif c == (")"):
                count -= 1
                if count == 0:
                    segments.append(temp)
                    temp = ""
                    if i < len(regex) - 1:
                        next = regex[i + 1]
                        if next != "*" and next != "|" and next != ")":
                            segments.append(".")
                    continue

            temp += c
            if count == 0:
                segments.append(temp)
                temp = ""
                if i < len(regex) - 1:
                    next = regex[i + 1]
                    if next != "*" and next != "|" and next != ")":
                        segments.append(".")

        return segments

    def _compileRegex(self):
        pass




