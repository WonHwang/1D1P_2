def is_donut(node, ins, outs):
    start = node
    
    while True:
        if len(ins[node]) != 1 or len(outs[node]) != 1:
            return False
        node = outs[node][0]
        
        if node == start:
            return True

def visit_donut(node, outs, visited):
    start = node
    
    while True:
        visited[node] = 1
        node = outs[node][0]
        if node == start:
            return

def is_stick(node, ins, outs):
    
    start = node
    
    if not outs[node] and not ins[node]:
        return True, node
    
    if not outs[node] and len(ins[node]) == 1:
        node = ins[node][0]
        while True:
            if len(outs[node]) == 1 and not ins[node]:
                return True, node
            elif len(outs[node]) == 1 and len(ins[node]) == 1:
                node = ins[node][0]
                if node == start:
                    return False, 0
            else:
                return False, 0
    
    if len(outs[node]) == 1 and len(ins[node]) == 1:
        node = ins[node][0]
        while True:
            if len(outs[node]) == 1 and not ins[node]:
                stick_start_node = node
                break
            elif len(outs[node]) == 1 and len(ins[node]) == 1:
                node = ins[node][0]
                if node == start:
                    return False, 0
            else:
                return False, 0
    
    if not ins[node] and len(outs[node]) == 1:
        stick_start_node = node
        node = outs[node][0]
        while True:
            if len(outs[node]) == 1 and len(ins[node]) == 1:
                node = outs[node][0]
            elif not outs[node] and len(ins[node]) == 1:
                return True, stick_start_node
            else:
                return False, 0
    
    if len(ins[node]) > 1 or len(outs[node]) > 1:
        return False, 0
    
    node = stick_start_node
    while True:
        if not outs[node]:
            return True, stick_start_node
        
        if outs[node]:
            node = outs[node][0]

def visit_stick(node, outs, visited):
    while True:
        visited[node] = 1
        if not outs[node]:
            return
        node = outs[node][0]

def is_eight(node, ins, outs):
    start = node
    while True:
        if len(outs[node]) == 2 and len(ins[node]) == 2:
            center = node
            break        
        elif len(outs[node]) == 1 and len(ins[node]) == 1:
            node = outs[node][0]
            if node == start:
                return False, 0
        else:
            return False, 0
        
    node = outs[center][0]
    while True:
        if len(outs[node]) == 2 and len(ins[node]) == 2 and node == center:
            break
        elif len(outs[node]) == 1 and len(ins[node]) == 1:
            node = outs[node][0]
        else:
            return False, 0
    
    node = outs[center][1]
    while True:
        if len(outs[node]) == 2 and len(ins[node]) == 2 and node == center:
            return True, center
        elif len(outs[node]) == 1 and len(ins[node]) == 1:
            node = outs[node][0]
        else:
            return False, 0

def visit_eight(node, outs, visited):
    center = node
    visited[center] = 1
    node = outs[center][0]
    while True:
        if node == center:
            break
        visited[node] = 1
        node = outs[node][0]
    
    node = outs[center][1]
    while True:
        if node == center:
            break
        visited[node] = 1
        node = outs[node][0]
        
def get_ins_outs(edges, point, Max):
    
    ins, outs = dict(), dict()
    for edge in edges:
        a, b = edge[0], edge[1]
        if a != point:
            if a != point and b != point:
                if outs.get(a):
                    outs[a].append(b)
                else:
                    outs[a] = [b]
                if ins.get(b):
                    ins[b].append(a)
                else:
                    ins[b] = [a]
    
    for node in range(1, Max+1):
        if not ins.get(node):
            ins[node] = []
        if not outs.get(node):
            outs[node] = []
    
    return ins, outs

def get_visited(point, Max):
    visited = dict()
    for i in range(1, Max+1):
        if i != point:
            visited[i] = 0
    
    return visited

def check_all_visited(point, visited, Max):
    for i in range(1, Max+1):
        if i != point:
            if not visited[i]:
                return False
    
    return True

def solution(edges):
    answer = []
    ins, outs = dict(), dict()
    Max = 0
    for edge in edges:
        a, b = edge[0], edge[1]
        if a > Max:
            Max = a
        if b > Max:
            Max = b
        if outs.get(a):
            outs[a].append(b)
        else:
            outs[a] = [b]
        if ins.get(b):
            ins[b].append(a)
        else:
            ins[b] = [a]
    for point in range(1, Max+1):
        if not ins.get(point):
            ins[point] = []
        if not outs.get(point):
            outs[point] = []
    
    for point in range(1, Max+1):
        ins_, outs_ = get_ins_outs(edges, point, Max)
        visited = get_visited(point, Max)
        d, s, e = 0, 0, 0
        for i in range(1, Max+1):
            if i != point and not visited[i]:
                if is_donut(i, ins_, outs_):
                    visit_donut(i, outs_, visited)
                    d += 1
                res, start = is_stick(i, ins_, outs_)
                if res:
                    visit_stick(start, outs_, visited)
                    s += 1
                res, start = is_eight(i, ins_, outs_)
                if res:
                    visit_eight(start, outs_, visited)
                    e += 1
        if (check_all_visited(point, visited, Max)):
            answer = [point, d, s, e]
            break
        
    return answer


def main():
    print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
    print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
    
if __name__ == '__main__':
    main()