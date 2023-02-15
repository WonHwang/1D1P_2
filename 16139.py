import sys
input = sys.stdin.readline
print = sys.stdout.write

S = input().rstrip()
q = int(input())
N = len(S)
arr = [[0 for _ in range(N)] for _ in range(26)]

for i in range(N):
    arr[ord(S[i])-ord('a')][i] += 1

for i in range(26):
    for j in range(1, N):
        arr[i][j] += arr[i][j-1]

for _ in range(q):
    target, start, end = map(str, input().split())
    start, end = int(start), int(end)
    
    if not start:
        print(f"{arr[ord(target)-ord('a')][end]}\n")
    
    else:
        print(f"{arr[ord(target)-ord('a')][end] - arr[ord(target)-ord('a')][start-1]}\n")