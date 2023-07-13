import sys

N = int(sys.stdin.readline().rstrip())
n, s, w, e = -10000, 10000, 10000, -10000

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if x < w:
        w = x
    if x > e:
        e = x
    if y > n:
        n = y
    if y < s:
        s = y

print((n-s)*(e-w))