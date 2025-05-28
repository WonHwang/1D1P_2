N = int(input())
DP = [0] * 101
DP[1] = 1
for i in range(2, 101):
    DP[i] = 2*DP[i-1] + 1

def hanoi(N, A, B, C):

    if N == 1:
        print(f"{A} {C}")
        return

    hanoi(N-1, A, C, B)
    print(f"{A} {C}")
    hanoi(N-1, B, A, C)

print(DP[N])
if N <= 20:
    hanoi(N, 1, 2, 3)