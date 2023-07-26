import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    
    left, right = 0, len(arr)-1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left

def LIS(N, A):
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
    
    return answer

N = int(input())
A, B = [], []
target = {}
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    A.append([a, b])
    target[b] = a

A.sort(key=lambda x:x[0])
for a in A:
    B.append(a[1])

lis = LIS(N, B)
result = {}
for b in B:
    result[b] = 0
for b in lis:
    result[b] = 1

answer = []
for key, value in result.items():
    if not value:
        answer.append(target[key])

answer.sort()
print(len(answer))
for num in answer:
    sys.stdout.write(str(num) + '\n')