import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

A = []
tree = [0] * 2400000

mod = 1000000007

for _ in range(N):
    A.append(int(input()))

def init(start, end, node):

    if start == end:
        tree[node] = A[start] % mod
    
    else:
        mid = (start + end) // 2
        tree[node] = (init(start, mid, 2*node) * init(mid+1, end, 2*node+1)) % mod
    
    return tree[node]

def get(start, end, left, right, node):

    if left > end or right < start:
        return 1
    
    if left <= start and end <= right:
        return tree[node] % mod
    
    mid = (start + end) // 2

    return (get(start, mid, left, right, 2*node) * get(mid+1, end, left, right, 2*node+1)) % mod

def change(start, end, node, idx, before, after, inverse):

    if start == idx and end == idx:
        if not before:
            tree[node] = after
        
        else:
            tree[node] *= inverse
            tree[node] %= mod
            tree[node] *= after
        
        tree[node] %= mod
        return
    
    if start <= idx <= end:

        mid = (start + end) // 2

        change(start, mid, 2*node, idx, before, after, inverse)
        change(mid+1, end, 2*node+1, idx, before, after, inverse)
        
        if not before:
            tree[node] = init(start, mid, 2*node) * init(mid+1, end, 2*node+1)
        
        else:
            tree[node] *= inverse
            tree[node] %= mod
            tree[node] *= after
        
        tree[node] %= mod

def get_inverse(before):

    binary = bin(mod-2)[2:][::-1]
    length = len(binary)
    DP = [1] * length

    for i in range(length):
        if binary[i] == "1":
            DP[i] = before

        before *= before
        before %= mod

    inverse = 1
    for i in range(length):
        inverse *= DP[i]
        inverse %= mod
    
    return inverse

init(0, N-1, 1)

for _ in range(M+K):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        idx = b-1
        before = A[idx]
        after = c
        A[idx] = after
        inverse = 0
        if before:
            inverse = get_inverse(before)

        change(0, N-1, 1, idx, before, after, inverse)
    
    elif a == 2:
        print(get(0, N-1, b-1, c-1, 1))