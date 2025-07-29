from collections import deque

ops = [" ", "+", "-"]

def calculate(exp):

    queue = deque(list(exp))
    stack = []
    digit = ""
    while queue:
        d = queue.popleft()
        if d in ops:
            if len(stack) > 1:
                op = stack.pop()
                num = stack.pop()
                if op == "+":
                    num += int(digit)
                elif op == "-":
                    num -= int(digit)
                stack.append(num)
                digit = ""
            else:
                stack.append(int(digit))
                digit = ""
            stack.append(d)
        else:
            digit += d
            
    if digit:
        if stack:
            op = stack.pop()
            num = stack.pop()
            if op == "+":
                num += int(digit)
            elif op == "-":
                num -= int(digit)
            stack.append(num)
            digit = ""
        else:
            stack.append(int(digit))
            digit = ""
    
    return stack.pop()

    


def build(N, select):

    exp = ""
    for i in range(N-1):
        exp += str(i+1)
        if select[i] == " ":
            continue
        exp += select[i]
    
    exp += str(N)
    res = calculate(exp)

    return res

def print_exp(N, select):

    exp = ""
    for i in range(N-1):
        exp += str(i+1)
        exp += select[i]
    exp += str(N)
    print(exp)

def dfs(N, depth, select):
    
    if depth == N-1:
        res = build(N, select)
        if not res:
            print_exp(N, select)
        return

    for op in ops:
        select[depth] = op
        dfs(N, depth+1, select)

for tc in range(int(input())):
    N = int(input())
    select = [""] * (N-1)
    dfs(N, 0, select)
    print()