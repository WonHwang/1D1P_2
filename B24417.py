N = int(input())
K = 1000000007
a, b = 1, 1
for _ in range(N-2):
    a, b = b%K, (a+b)%K
print(b, N-2)