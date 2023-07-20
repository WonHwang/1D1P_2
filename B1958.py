A = input()
B = input()
C = input()
N, M, L = len(A), len(B), len(C)

lcs = [[[0 for _ in range(L+1)] for _ in range(M+1)] for _ in range(N+1)]

Max = 0
for i in range(N+1):
    for j in range(M+1):
        for k in range(L+1):

            if i == 0 or j == 0 or k == 0:
                lcs[i][j][k] = 0
            
            elif A[i-1] == B[j-1] and B[j-1] == C[k-1]:
                lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
                if lcs[i][j][k] > Max:
                    Max = lcs[i][j][k]
            
            else:
                lcs[i][j][k] = max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1], lcs[i-1][j][k-1], lcs[i][j-1][k-1], lcs[i-1][j-1][k])

print(Max)