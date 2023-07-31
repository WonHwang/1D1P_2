import sys
input = sys.stdin.readline

N = int(input())

dance = set()
dance.add("ChongChong")
for _ in range(N):
    a, b = map(str, input().rstrip().split())
    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)

print(len(dance))