n, d = map(int, input().split())
answer = 0

def dfs(now, cnt):

    global answer

    if now > n:
        return
    
    answer += cnt

    for i in range(10):
        if i == d:
            dfs(10*now+i, cnt+1)
        else:
            dfs(10*now+i, cnt)

for i in range(1, 10):
    if i == d:
        dfs(i, 1)
    else:
        dfs(i, 0)

print(answer)