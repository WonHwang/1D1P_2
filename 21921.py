N, X = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * N
prefix[0] = arr[0]
for i in range(N-1):
    prefix[i+1] = prefix[i] + arr[i+1]
prefix = [0] + prefix

Max = 0
cnt = 0
for i in range(N-X+1):
    start, end = i, i+X
    tmp = prefix[end]-prefix[start]
    if tmp > Max:
        Max = tmp
        cnt = 1
    elif tmp == Max:
        cnt += 1
        
if Max:
    print(Max)
    print(cnt)
else:
    print("SAD")