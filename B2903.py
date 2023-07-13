N = int(input())
arr = [0] * 16
arr[0] = 2
for i in range(1, N+1):
    arr[i] = 2 * arr[i-1] - 1

print(arr[N] ** 2)