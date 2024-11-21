import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
dic = dict()
for _ in range(N):
    word, deg = map(str, input().rstrip().split())
    deg = int(deg)
    dic[deg] = dic.get(deg, word)

IF = []
for deg in dic:
    IF.append([dic[deg], deg])
N = len(IF)

for _ in range(M):
    score = int(input())
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if IF[mid][1] > score:
            end = mid-1
        else:
            start = mid+1
    for i in range(max(mid-2, 0), N):
        if score <= IF[i][1]:
            print(f"{IF[i][0]}\n")
            break