N = int(input())
nums = list(map(int, input().split()))
answer = 0

def dfs(depth, res):
    
    global answer
    
    if not (0 <= res <= 20):
        return
    
    if depth == N-1:
        if res == nums[depth]:
            answer += 1
        return
    
    dfs(depth+1, res+nums[depth])
    dfs(depth+1, res-nums[depth])

dfs(0, 0)
print(answer)