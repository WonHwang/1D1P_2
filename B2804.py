A, B = map(str, input().split())
x, y = -1, -1
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            x, y = i, j
            break
    if x != -1 and y != -1:
        break

answer = [['.' for _ in range(len(A))] for _ in range(len(B))]
for i in range(len(A)):
    answer[y][i] = A[i]
for j in range(len(B)):
    answer[j][x] = B[j]

for i in range(len(answer)):
    print(''.join(answer[i]))