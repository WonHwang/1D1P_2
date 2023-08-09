import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
tree = [0] * 300000

def get_min_idx(a, b):

    if a == -1:
        return b
    
    if b == -1:
        return a

    if A[a] > A[b]:
        idx = b
    elif A[a] < A[b]:
        idx = a
    else:
        idx = min(a, b)
    
    return idx


def init(start, end, node):

    if start == end:
        tree[node] = start
    
    else:
        mid = (start + end) // 2

        a, b = init(start, mid, 2*node), init(mid+1, end, 2*node+1)

        idx = get_min_idx(a, b)
        
        tree[node] = idx
    
    return tree[node]

def get(start, end, left, right, node):

    if start > right or left > end:
        return -1
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2

    a, b = get(start, mid, left, right, 2*node), get(mid+1, end, left, right, 2*node+1)

    idx = get_min_idx(a, b)

    return idx

def change(start, end, node, idx):

    if start == idx and idx == end:
        return
    
    if start <= idx <= end:

        mid = (start + end) // 2

        change(start, mid, 2*node, idx)
        change(mid+1, end, 2*node+1, idx)

        a, b = get(start, mid, start, mid, 2*node), get(mid+1, end, mid+1, end, 2*node+1)

        i = get_min_idx(a, b)

        tree[node] = i

init(0, N-1, 1)

M = int(input())

for _ in range(M):
    c, i, j = map(int, input().rstrip().split())

    if c == 1:

        idx = i-1
        A[idx] = j

        change(0, N-1, 1, idx)
    
    elif c == 2:
        print(get(0, N-1, i-1, j-1, 1)+1)