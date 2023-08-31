N, M, G = map(int, input().split())

nums = list(map(int, input().split()))

answer = 0

def dfs(total, depth, cnt):
    
    global answer

    if cnt > M:
        return
    
    if depth >= N:
        if cnt == M:
            if total <= G and total > answer:
                answer = total
        return
    
    dfs(total+nums[depth], depth+1, cnt+1)
    dfs(total, depth+1, cnt)

dfs(0, 0, 0)

print(answer)
