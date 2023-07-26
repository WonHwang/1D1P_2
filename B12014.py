def lower_bound(arr, target):
    
    left, right = 0, len(arr)-1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left

def LIS(arr, N):

    DP = [arr[0]]
    for i in range(1, N):
        
        if arr[i] > DP[-1]:
            DP.append(arr[i])
        else:
            idx = lower_bound(DP, arr[i])
            DP[idx] = arr[i]

    return len(DP)

for t in range(1, int(input())+1):

    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    Max = LIS(arr, N)
    print(f"Case #{t}")
    print(1 if Max >= K else 0)