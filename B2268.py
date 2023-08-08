import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
A = [0] * N
tree = [0] * 2500000


def init(start, end, node):

    if start == end:
        tree[node] = A[start]
    
    else:
        mid = (start + end) // 2

        tree[node] = init(start, mid, 2*node) + init(mid+1, end, 2*node+1)
    
    return tree[node]

def get(start, end, left, right, node):

    if start > right or left > end:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2

    return get(start, mid, left, right, 2*node) + get(mid+1, end, left, right, 2*node+1)

def change(start, end, node, diff, idx):

    if start == idx and idx == end:
        tree[node] += diff
        return
    
    if start <= idx <= end:

        mid = (start + end) // 2

        change(start, mid, 2*node, diff, idx)
        change(mid+1, end, 2*node+1, diff, idx)

        tree[node] += diff

init(0, N-1, 1)
for _ in range(Q):

    a, b, c = map(int, input().rstrip().split())

    if a == 0:
        if b > c:
            b, c = c, b
        print(get(0, N-1, b-1, c-1, 1))
    
    else:
        idx = b-1
        diff = c - A[idx]
        A[idx] = c
        change(0, N-1, 1, diff, idx)