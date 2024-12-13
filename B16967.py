import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
B = []
for _ in range(H+X):
    B.append(list(map(int, input().split())))

for i in range(H):
    for j in range(W):
        B[i+X][j+Y] -= B[i][j]

for i in range(H):
    for j in range(W):
        print(B[i][j], end=' ')
    print()