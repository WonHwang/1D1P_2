import sys
input = sys.stdin.readline

tree = [0] * 2097154
A = []
N, M, K = map(int, input().rstrip().split())

def init(start, end, node):

    if start == end:
        tree[node] = A[start]
    
    else:
        mid = (start + end) // 2

        tree[node] = init(start, mid, 2*node) + init(mid+1, end, 2*node+1)
    
    return tree[node]

def get(start, end, left, right, node):

    if end < left or start > right:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2

    return get(start, mid, left, right, 2*node) + get(mid+1, end, left, right, 2*node+1)

def change(start, end, node, idx, diff):

    if start == idx and idx == end:
        tree[node] += diff
        return
    
    if start <= idx <= end:
        tree[node] += diff

        mid = (start + end) // 2

        change(start, mid, 2*node, idx, diff)
        change(mid+1, end, 2*node+1, idx, diff)

for _ in range(N):
    A.append(int(input()))

init(0, N-1, 1)

for _ in range(M+K):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        idx = b - 1
        diff = c - A[idx]
        A[idx] = c
        change(0, N-1, 1, idx, diff)
    
    elif a == 2:
        print(get(0, N-1, b-1, c-1, 1))