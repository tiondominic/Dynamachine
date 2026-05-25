import State

class NFAState(State.State):
    def add_transition(self, at, state):
        if at not in self.transitions:
            self.transitions[at] = []
        self.transitions[at].append(state)

class Fragment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class NFA:
    def __init__(self, regex):
        self.regex = regex
        self.counter = 0
        self.start_state = self._regex_to_nfa(regex).start

    def _regex_to_nfa(self, regex):
        if regex == "":
            start = NFAState("", False)
            start.end_state = True
            return Fragment(start, start)

        if len(regex) == 1 and regex not in ("*", "|", "."):
            print(f"processing fragment {regex}")

            start = NFAState(f"q{self.counter}", False)
            end = NFAState(f"q{self.counter + 1}", True)
            self.counter += 2

            start.add_transition(regex, end)

            return Fragment(start, end)

        segs = self.parse_regex(regex)
        print(segs)

        nfa_frags = []
        operations = []

        for seg in segs:
            print(f"processing seg {seg}")
            if seg not in ("*", ".", "|"):
                frag = self._regex_to_nfa(seg)
                nfa_frags.append(frag)
                print("Fragment creation done")

            elif seg == "*":

                old_nfa = nfa_frags.pop()

                old_nfa.end.end_state = False

                new_start = NFAState(f"q{self.counter}", False)
                new_end = NFAState(f"q{self.counter + 1}", True)
                self.counter += 2

                new_start.add_transition("$", old_nfa.start)
                new_start.add_transition("$", new_end)

                old_nfa.end.add_transition("$", old_nfa.start)
                old_nfa.end.add_transition("$", new_end)

                nfa_frags.append(Fragment(new_start, new_end))

            elif seg in (".", "|"):
                print(f"adding {seg} to operations")
                operations.append(seg)
                continue


            i = len(operations)
            print(f"Condition check {i} {len(nfa_frags)}")
            print(segs)

            while i > 0 and len(nfa_frags) >= 2:
                print(f"Processing operation: {operations[-1]}")
                if operations[-1] == ".":
                    operations.pop()

                    frag1 = nfa_frags.pop()
                    frag2 = nfa_frags.pop()

                    frag2.end.end_state = False

                    frag2.end.add_transition("$", frag1.start)

                    combined = Fragment(frag2.start, frag1.end)
                    print(f"processed concatenation operation")
                    print(combined.end.transitions, combined.end.transitions)

                    nfa_frags.append(combined)

                else:
                    i -= 1

        i = 0

        while i < len(operations) and len(nfa_frags) >= 2:
            if operations[-1] == "|":
                operations.pop()
                frag1 = nfa_frags.pop()
                frag2 = nfa_frags.pop()

                frag1.end.end_state = False
                frag2.end.end_state = False

                new_start = NFAState(f"q{self.counter}", False)
                new_end = NFAState(f"q{self.counter + 1}", True)
                self.counter += 2

                new_start.add_transition("$", frag1.start)
                new_start.add_transition("$", frag2.start)

                frag1.end.add_transition("$", new_end)
                frag2.end.add_transition("$", new_end)

                combined = Fragment(new_start, new_end)

                nfa_frags.append(combined)
            else:
                i += 1
        print(f"Returning: {nfa_frags[0].start}")
        return nfa_frags[0]

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
            elif c == ")":
                count -= 1
                if count == 0:
                    segments.append(temp)
                    temp = ""
                    if i < len(regex) - 1:
                        next = regex[i + 1]
                        if next != "*" and next != "|" and next != ")" and c != "|":
                            segments.append(".")
                    continue

            temp += c
            if count == 0:
                segments.append(temp)
                temp = ""
                if i < len(regex) - 1:
                    next = regex[i + 1]
                    if next != "*" and next != "|" and next != ")" and c != "|":
                        segments.append(".")

        return segments




