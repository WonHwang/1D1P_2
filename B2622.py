N = int(input())
answer = 0
for i in range(1, (N//3)+1):
    for j in range((N-i)//2, i-1, -1):
        k = N-i-j
        if i+j > k:
            answer += 1
        else:
            break
print(answer)