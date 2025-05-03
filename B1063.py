direc = {
    'R': [0, 1],
    'L': [0, -1],
    'B': [-1, 0],
    'T': [1, 0],
    'RT': [1, 1],
    'LT': [1, -1],
    'RB': [-1, 1],
    'LB': [-1, -1]
}

def get_grid(x):
    a, b = x[0], int(x[1])-1
    a = ord(a)-ord('A')
    
    return b, a

king, stone, N = map(str, input().split())
kx, ky = get_grid(king)
sx, sy = get_grid(stone)
N = int(N)

for _ in range(N):
    d = direc.get(input())
    a, b = d[0], d[1]
    
    x, y = kx + a, ky + b
    if 0 <= x < 8 and  0 <= y < 8:
        if not (x == sx and y == sy):
            kx, ky = x, y
        
        else:
            x_, y_ = sx + a, sy + b
            if 0 <= x_ < 8 and 0 <= y_ < 8:
                kx, ky = x, y
                sx, sy = x_, y_

print(f"{chr(ord('A')+ky)}{kx+1}")
print(f"{chr(ord('A')+sy)}{sx+1}")