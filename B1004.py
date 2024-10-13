import sys
input = sys.stdin.readline

def get_distance_square(a, b, x, y):
    
    return ((a-x)**2) + ((b-y)**2)

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
        
    answer = 0
    for i in range(N):
        x, y, r = data[i][0], data[i][1], data[i][2]
        r **= 2
        start, end = get_distance_square(x1, y1, x, y), get_distance_square(x2, y2, x, y)
        
        if (start < r and end > r) or (start > r and end < r):
            answer += 1
    
    print(answer)