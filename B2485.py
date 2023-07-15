def get_gcd(a, b):
    if b > a:
        a, b = b, a
    
    while b:
        a, b = b, a%b
    
    return a

N = int(input())
tree = []
for _ in range(N):
    tree.append(int(input()))

tree.sort()

gcd = tree[1] - tree[0]
for i in range(2, N):
    gap = tree[i] - tree[i-1]
    gcd = get_gcd(gcd, gap)

print(((tree[-1] - tree[0]) // gcd) - N + 1)