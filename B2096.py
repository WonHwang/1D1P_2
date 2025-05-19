import sys
input = sys.stdin.readline

N = int(input())
A, B, C = -1, -1, -1
a, b, c = -1, -1, -1
for i in range(N):
    x, y, z = map(int, input().split())
    if i == 0:
        A, B, C, a, b, c = x, y, z, x, y, z
        continue
    A, B, C = x + max(A, B), y + max(A, B, C), z + max(B, C)
    a, b, c = x + min(a, b), y + min(a, b, c), z + min(b, c)

print(max(A, B, C), min(a, b, c))