N, K = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0] * 100001
start, end = 0, 0
answer = 0
while start <= end and end < N:
    
    if visited[nums[end]] < K:
        visited[nums[end]] += 1
        end += 1
    
    else:
        visited[nums[start]] -= 1
        start += 1

    size = end - start
    if size > answer:
        answer = size
    
print(answer)