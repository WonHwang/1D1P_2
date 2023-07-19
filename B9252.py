A = input()
B = input()
N, M = len(A), len(B)

Max = 0
lcs = [[[0, []] for _ in range(M+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(M+1):

        if i == 0 or j == 0:
            lcs[i][j] = [0, []]
        
        elif A[i-1] == B[j-1]:
            lcs[i][j][0] = lcs[i-1][j-1][0] + 1
            lcs[i][j][1] = lcs[i-1][j-1][1]
            lcs[i][j][1].append(i-1)
            if lcs[i][j][0] > Max:
                Max = lcs[i][j][0]
        
        else:
            if lcs[i-1][j][0] > lcs[i][j-1][0]:
                lcs[i][j][0] = lcs[i-1][j][0]
                lcs[i][j][1] = lcs[i-1][j][1]
            else:
                lcs[i][j][0] = lcs[i][j-1][0]
                lcs[i][j][1] = lcs[i][j-1][1]

answer = ""
target = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if lcs[i][j][0] == Max:
            target = lcs[i][j][1]
            break
    if target:
        break
for num in target:
    answer += A[num]
    
print(Max)
print(answer)