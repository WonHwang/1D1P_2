import sys
input = sys.stdin.readline

N, X = map(str, input().split())
N = int(N)
Set = set()
for _ in range(N):
    Set.add(input().rstrip())

M = len(Set)
if X == 'Y':
    print(M)
elif X == 'F':
    print(M//2)
elif X == 'O':
    print(M//3)