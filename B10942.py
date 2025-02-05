import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
DP = [[0 for _ in range(N)] for _ in range(N)]

# DP 채우는 for문 깔끔하게 하려고 미리 1개, 2개 짜리는 처리
for i in range(N):
    DP[i][i] = 1

for i in range(N-1):
    if nums[i] == nums[i+1]:
        DP[i][i+1] = 1

# 판단 기준이 nums[start] == nums[end] and DP[start+1][end-1] == 1 이므로 작은 사이즈부터 채워가는 게 포인트
for size in range(2, N):
    for start in range(N-size):
        end = start + size

        if nums[start] == nums[end]:
            if DP[start+1][end-1]:
                DP[start][end] = 1

for _ in range(int(input())):
    S, E = map(int, input().split())
    print(DP[S-1][E-1])


'''
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7

1
0
1
1
'''