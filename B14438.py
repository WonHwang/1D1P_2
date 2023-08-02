import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
tree = [0] * 300000

def init(start, end, node):

    if start == end:

        tree[node] = A[start]
    
    else:

        mid = (start + end) // 2
        tree[node] = min(init(start, mid, 2*node), init(mid+1, end, 2*node+1))
    
    return tree[node]

def get(start, end, left, right, node):

    if start > right or left > end:
        return 1000000001
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2

    return min(get(start, mid, left, right, 2*node), get(mid+1, end, left, right, 2*node+1))

def change(start, end, node, idx, value):

    if start == idx and idx == end:
        tree[node] = value
        return
    
    if start <= idx <= end:

        mid = (start + end) // 2

        change(start, mid, 2*node, idx, value)
        change(mid+1, end, 2*node+1, idx, value)

        tree[node] = min(tree[2*node], tree[2*node+1])
        return

init(0, N-1, 1)

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    if a == 1:
        idx = b - 1
        value = c
        A[idx] = c

        change(0, N-1, 1, idx, value)
    
    elif a == 2:
        print(get(0, N-1, b-1, c-1, 1))