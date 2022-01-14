# 1D1P Day4 1051번 숫자 정사각형

N, M = map(int, input().split())
rectangle = []
for i in range(N):
    rectangle.append(list(input()))
    for j in range(M):
        rectangle[i][j] = int(rectangle[i][j])

if N > M:
    tmp1 = []
    for i in range(M):
        tmp2 = []
        for j in range(N):
            tmp2.append(rectangle[j][i])
        tmp1.append(tmp2)
    
    rectangle = tmp1
    N, M = M, N

size = N

answer = 0
while True:

    if size == 1:
        answer = 1
        break

    for i in range(N-size+1):
        for j in range(M-size+1):
            if rectangle[i][j] == rectangle[i][j+size-1] == rectangle[i+size-1][j] == rectangle[i+size-1][j+size-1]:
                answer = size
                break
        if answer:
            break
    if answer:
        break

    size -= 1

print(answer**2)