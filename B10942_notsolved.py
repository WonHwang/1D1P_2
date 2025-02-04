import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
DP = [[-1 for _ in range(N)] for _ in range(N)]

def is_pal(S, E):

    if nums[S] != nums[E]:
        DP[S][E] = 0
        return False
    
    if S == E:
        DP[S][E] = 1
        return True

    if nums[S] == nums[E]:
        if S+1 == E:
            DP[S][E] = 1
            return True

        if DP[S+1][E-1] == -1 and is_pal(S+1, E-1):
            DP[S][E] = 1
            return True
        
        else:
            DP[S][E] = 0
            return False

def do_dp(S, E):

    if S == E:
        DP[S][E] = 1
        return

    if DP[S][E] == -1:
        is_pal(S, E)
    
    do_dp(S+1, E)
    do_dp(S, E-1)

do_dp(0, N-1)

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