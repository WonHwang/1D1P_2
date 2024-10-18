import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(dic, x):
    if dic[x] == x:
        return x
    
    dic[x] = find(dic, dic[x])
    return dic[x]

def union(rank, dic, x, y):
    a, b = find(dic, x), find(dic, y)

    if a == b:
        return

    if rank[a] < rank[b]:
        a, b = b, a
    
    dic[b] = a
    rank[a] += rank[b]

for tc in range(int(input())):

    dic = dict()
    rank = dict()
    for F in range(int(input())):
        x, y = map(str, input().rstrip().split())
        if not dic.get(x):
            dic[x] = x
            rank[x] = 1
        if not dic.get(y):
            dic[y] = y
            rank[y] = 1
        
        union(rank, dic, x, y)
        root = find(dic, x)
        print(rank[root])