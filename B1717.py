import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(graph, x):

    if graph[x] == x:
        return x
    
    graph[x] = find(graph, graph[x])
    return graph[x]

def union(graph, x, y):
    graph[find(graph, x)] = find(graph, y)

def is_union(graph, x, y):
    return find(graph, x) == find(graph, y)

N, M = map(int, input().split())
graph = [i for i in range(N+1)]

for _ in range(M):
    op, a, b = map(int, input().split())
    print("YES" if is_union(graph, a, b) else "NO") if op else union(graph, a, b)