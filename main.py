import NFA

a = NFA.NFA("(ab|c)*ab((abc)|(cdc)*)")
c = a.parse_regex("(ab|c)*ab((abc)|(cdc)*)")

print(c)