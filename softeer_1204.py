N, B = map(int, input().split())
com = list(map(int, input().split()))
com.sort()
left, right = 1, 10**18 + 10**9 + 1
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    d = 0
    for i in range(N):
        if com[i] < mid:
            d += abs(com[i] - mid) ** 2
    
    if d <= B:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)