def lower_bound(arr, target):
    
    left, right = 0, len(arr)-1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left

def LIS(arr):

    N = len(arr)
    DP = [arr[0]]
    for i in range(1, N):
        
        if arr[i] > DP[-1]:
            DP.append(arr[i])
        else:
            idx = lower_bound(DP, arr[i])
            DP[idx] = arr[i]

    return len(DP)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [0] * N
for i in range(N):
    C[A[i]-1] = i

for i in range(N):
    B[i] = C[B[i]-1]

print(LIS(B))