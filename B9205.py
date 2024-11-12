from collections import deque

def get_distance(a, b, c, d):
    return abs(a-c) + abs(b-d)

for tc in range(int(input())):
    n = int(input())
    x, y = map(int, input().split())
    conv = []
    for _ in range(n):
        conv.append(list(map(int, input().split())))
    ex, ey = map(int, input().split())
    queue = deque()
    visited = [0] * n
    queue.append([x, y])
    answer = False
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        if get_distance(x, y, ex, ey) <= 1000:
            answer = True
            break

        for i in range(n):
            a, b = conv[i][0], conv[i][1]
            if not visited[i] and get_distance(x, y, a, b) <= 1000:
                visited[i] = 1
                queue.append([a, b])
    
    print('happy' if answer else 'sad')