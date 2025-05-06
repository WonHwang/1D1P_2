N, M = map(int, input().split())
left, right = 1, M
answer = 0
for _ in range(int(input())):
    t = int(input())
    while True:
        if left <= t <= right:
            break
        
        if t > right:
            left += 1
            right += 1
        
        else:
            left -= 1
            right -= 1
        
        answer += 1

print(answer)