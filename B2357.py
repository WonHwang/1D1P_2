import sys
input = sys.stdin.readline

max_tree = [0] * 500000
min_tree = [0] * 500000
Max = 0
Min = 1000000000
A = []

N, M = map(int, input().rstrip().split())

for _ in range(N):
    num = int(input())
    A.append(num)
    if num > Max:
        Max = num
    if num < Min:
        Min = num

def min_init(start, end, node):

    if start == end:
        min_tree[node] = A[start]

    else:
        mid = (start + end) // 2

        min_tree[node] = min(min_init(start, mid, 2*node), min_init(mid+1, end, 2*node+1))
    
    return min_tree[node]

def max_init(start, end, node):

    if start == end:
        max_tree[node] = A[start]
    
    else:
        mid = (start + end ) // 2

        max_tree[node] = max(max_init(start, mid, 2*node), max_init(mid+1, end, 2*node+1))
    
    return max_tree[node]

min_init(0, N-1, 1)
max_init(0, N-1, 1)

def get_min(start, end, left, right, node):

    if left > end or right < start:
        return Max
    
    if left <= start and end <= right:
        return min_tree[node]
    
    mid = (start + end) // 2

    return min(get_min(start, mid, left, right, 2*node), get_min(mid+1, end, left, right, 2*node+1))

def get_max(start, end, left, right, node):

    if left > end or right < start:
        return Min
    
    if left <= start and end <= right:
        return max_tree[node]
    
    mid = (start + end) // 2

    return max(get_max(start, mid, left, right, 2*node), get_max(mid+1, end, left, right, 2*node+1))

for _ in range(M):

    a, b = map(int, input().rstrip().split())
    print(get_min(0, N-1, a-1, b-1, 1), get_max(0, N-1, a-1, b-1, 1))