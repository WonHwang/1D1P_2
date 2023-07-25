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
idx_arr = [0]

for i in range(1, N):
    
    if A[i] > DP[-1]:
        DP.append(A[i])
        idx_arr.append(len(DP)-1)
    else:
        idx = lower_bound(DP, A[i])
        DP[idx] = A[i]
        idx_arr.append(idx)

target = len(DP)-1
idx = N-1
answer = []
while True:

    if idx == -1:
        break

    if idx_arr[idx] == target:
        answer.append(A[idx])
        target -= 1
    idx -= 1

print(len(DP))
print(*answer[::-1])