def lower_bound(arr, target):
    
    left, right = 0, len(arr)-1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left

N = int(input())
A = list(map(int, input().split()))
DP = []
DP.append(A[0])

for i in range(1, N):
    
    if A[i] > DP[-1]:
        DP.append(A[i])
    else:
        idx = lower_bound(DP, A[i])
        DP[idx] = A[i]

print(len(DP))