N = int(input())
M = int(input())
disable = []
if M:
    disable = list(map(int, input().split()))
btn = [str(i) for i in range(10) if i not in disable]
size = len(str(N))
answer = abs(100-N)

def dfs(now, size):

    global answer

    if len(now) == size:
        tmp = abs(int(now)-N)+size
        if tmp < answer:
            answer = tmp
        return

    for b in btn:
        dfs(now+b, size)

if size > 1:
    dfs("", size-1)
dfs("", size)
if size < 6:
    dfs("", size+1)

print(answer)