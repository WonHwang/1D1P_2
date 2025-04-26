combi = {
    "AA": "A",
    "AG": "C",
    "AC": "A",
    "AT": "G",
    "GA": "C",
    "GG": "G",
    "GC": "T",
    "GT": "A",
    "CA": "A",
    "CG": "T",
    "CC": "C",
    "CT": "G",
    "TA": "G",
    "TG": "A",
    "TC": "G",
    "TT": "T"
}

N = int(input())
stack = list(input())
while len(stack) >= 2:
    b = stack.pop()
    a = stack.pop()
    c = combi.get(a+b)
    stack.append(c)
print(stack.pop())