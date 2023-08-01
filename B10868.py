import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

tree = [0] * 300000
A = []

for _ in range(N):
    A.append(int(input()))

def init(start, end, node):

    if start == end:
        tree[node] = A[start]
    
    else:
        mid = (start + end) // 2

        tree[node] = min(init(start, mid, 2*node), init(mid+1, end, 2*node+1))
    
    return tree[node]

def get(start, end, left, right, node):

    if end < left or start > right:
        return 1000000001
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2

    return min(get(start, mid, left, right, 2*node), get(mid+1, end, left, right, 2*node+1))

init(0, N-1, 1)

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    print(get(0, N-1, a-1, b-1, 1))