import sys
input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
    points.append(list(map(int, input().split())))

answer = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            a, b, c = points[i], points[j], points[k]
            x1, y1, x2, y2, x3, y3 = a[0], a[1], b[0], b[1], c[0], c[1]
            d1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
            d2 = (x1 - x3) ** 2 + (y1 - y3) ** 2
            d3 = (x2 - x3) ** 2 + (y2 - y3) ** 2
            
            if d1 == d2+d3 or d2 == d1+d3 or d3 == d1+d2:
                answer += 1

print(answer)