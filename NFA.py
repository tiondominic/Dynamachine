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
        self.regex = regex
        self._regexToNFA(regex)

    def _regexToNFA(self, regex):
        if regex == "":
            start = State("", False)
            start.end_state = True
            return Fragment(start, start)

        if len(regex) == 1 and regex not in ("*", "|", "."):
            start = State("", False)
            end = State("", True)

            start._addTransition(regex, end)

            return Fragment(start, end)

        segs = self.parse_regex(regex)

        nfa_frags = []
        operations = []

        for seg in segs:
            if seg not in ("*", ".", "|"):
                frag = self._regexToNFA(seg)
                nfa_frags.append(frag)

            elif seg == "*":

                old_nfa = nfa_frags.pop()

                old_nfa.end.end_state = False

                new_start = State("", False)
                new_end = State("", True)

                new_start._addTransition("$", old_nfa.start)
                new_start._addTransition("$", new_end)

                old_nfa.end._addTransition("$", old_nfa.start)
                old_nfa.end._addTransition("$", new_end)

                nfa_frags.append(Fragment(new_start, new_end))

            elif seg in (".", "|"):
                operations.append(seg)

        i = 0

        while i < len(operations) and len(nfa_frags) > 2:
            if operations[i] == ".":

                frag1 = nfa_frags[i]
                frag2 = nfa_frags[i + 1]

                frag1.end.end_state = False

                frag1.end._addTransition("$", frag2.start)

                combined = Fragment(frag1.start, frag2.end)

                nfa_frags[i] = combined
                nfa_frags.pop(i + 1)

                operations.pop(i)

            else:
                i += 1

        i = 0

        while i < len(operations):
            if operations[i] == "|":

                frag1 = nfa_frags[i]
                frag2 = nfa_frags[i + 1]

                frag1.end.end_state = False
                frag2.end.end_state = False

                new_start = State("", False)
                new_end = State("", True)

                new_start._addTransition("$", frag1.start)
                new_start._addTransition("$", frag2.start)

                frag1.end._addTransition("$", new_end)
                frag2.end._addTransition("$", new_end)

                combined = Fragment(new_start, new_end)

                nfa_frags[i] = combined
                nfa_frags.pop(i + 1)

                operations.pop(i)

            else:
                i += 1

        self.start_state = nfa_frags[0].start

    def validate_string(self, string):
        current_states = set()
        current_states.add(self.start_state)

        current_states = self._epsilon_closure(current_states)

        for char in string:
            next_states = set()
            for state in current_states:
                if char in state.transitions:
                    for next_state in state.transitions[char]:
                        next_states.add(next_state)

            current_states = self._epsilon_closure(next_states)
        for state in current_states:
            if state.end_state:
                return True

        return False

    def _epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)

        while stack:
            state = stack.pop()
            if "$" in state.transitions:
                for next_state in state.transitions["$"]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def parse_regex(self, regex):
        count = 0
        temp = ""
        segments = []

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




