from collections import deque

def init_visited(visited):
    for key in visited:
        visited[key] = 0

def is_all_visited(visited):
    for key in visited:
        if not visited.get(key):
            return False
    return True

def is_donut(node, connection, visited):
    
    start = node
    queue = deque()
    queue.append(node)
    visited[node] = 1
    
    while queue:
        node = queue.popleft()
        
        if len(connection[node]) != 1:
            return False
        
        node = connection[node][0]
        if not visited[node]:
            visited[node] = 1
            queue.append(node)
        
        else:
            if node == start:
                return True
    
    return False

def is_stick(node, connection, visited):
    
    queue = deque()
    queue.append(node)
    visited[node] = 1
    
    while queue:
        node = queue.popleft()
        
        if not len(connection[node]):
            return True
        
        if len(connection[node]):
            return False
        
        node = connection[node][0]
        
        if visited[node]:
            return False
        
        visited[node] = 1
        queue.append(node)

    return False

def is_eight(node, connection, visited):
    
    center = 0
    visited = [0] * 1000001
    visited[node] = 1
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        if len(connection[node]) == 2:
            center = node
            break
        
        if len(connection[node]) == 1:
            node = connection[node][0]
            if not visited[node]:
                visited[node] = 1
                queue.append(node)
            else:
                return False
            
    if not center:
        return False
    
    cnt1 = 0
    visited = [0] * 1000001
    visited[center] = 1
    node = connection[center][0]
    visited[node] = 1
    while True:
        if len(connection[node]) == 2:
            if node == center:
                break
        
        if len(connection[node]) != 1:
            return False
        
        node = connection[node][0]
        visited[node] = 1
        cnt1 += 1
    
    cnt2 = 0
    visited = [0] * 1000001
    visited[center] = 1
    node = connection[center][1]
    visited[node] = 1
    while True:
        if len(connection[node]) == 2:
            if node == center:
                break
        
        if len(connection[node]) != 1:
            return False
        
        node = connection[node][0]
        visited[node] = 1
        cnt2 += 1
    
    if cnt1 != cnt2:
        return False
    
    return True

def solution(edges):
    print(edges)
    answer = [0, 0, 0, 0]
    connection = [[] for _ in range(1000001)]
    visited = dict()
    Max = 0
    for edge in edges:
        a, b = edge[0], edge[1]
        if a > Max:
            Max = a
        if b > Max:
            Max = b
        connection[a].append(b)
        visited[a] = 0
        visited[b] = 0

    for point in range(1, Max+1):
        print("-----------------------")
        print(f"point: {point} start")
        donut, stick, eight = 0, 0, 0
        init_visited(visited)
        visited[point] = 1
        for node in connection[point]:
            if is_donut(node, connection, visited):
                print(f"node: {node} is donut")
                donut += 1
            elif is_stick(node, connection, visited):
                print(f"node: {node} is stick")
                stick += 1
            elif is_eight(node, connection, visited):
                print(f"node: {node} is eight")
                eight += 1
            else:
                print(f"node: {node} is nothing")
                donut, stick, eight = 0, 0, 0
                break
        
        if is_all_visited(visited):
            if donut or stick or eight:
                answer = [point, donut, stick, eight]
                break
        
        print(f"{point} is not point")
        
    return answer


def main():
    print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
    print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
    
if __name__ == '__main__':
    main()