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

while True:

    try:
        N = int(input())
        A = list(map(int, input().split()))
        print(LIS(A, N))
    
    except:
        break