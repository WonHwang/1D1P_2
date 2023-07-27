import sys
input = sys.stdin.readline

def lower_bound(arr, T):

    left, right = 0, len(arr)-1

    while left < right:

        mid = (left + right) // 2

        if arr[mid] >= T:
            right = mid
        
        else:
            left = mid + 1
    
    return right

def get_len_lis(arr):

    N = len(arr)
    DP = [arr[0]]

    for i in range(1, N):

        if arr[i] > DP[-1]:
            DP.append(arr[i])
        else:
            idx = lower_bound(DP, arr[i])
            DP[idx] = arr[i]
    
    return len(DP)

for _ in range(int(input())):

    N = int(input())
    arr = []

    for _ in range(N):
        arr.append(int(input()))
    
    print(get_len_lis(arr))