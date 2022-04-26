dice = {i:0 for i in range(1, 7)}
shape = [i for i in range(1, 7)]

def roll(shape, direction):
    
    tmp = [0] * 6
    
    if direction == 1:
        
        tmp[0] = shape[3]
        tmp[1] = shape[1]
        tmp[2] = shape[0]
        tmp[3] = shape[5]
        tmp[4] = shape[4]
        tmp[5] = shape[2]
    
    if direction == 2:
        
        tmp[0] = shape[2]
        tmp[1] = shape[1]
        tmp[2] = shape[5]
        tmp[3] = shape[0]
        tmp[4] = shape[4]
        tmp[5] = shape[3]
        
    if direction == 3:
        
        tmp[0] = shape[4]
        tmp[1] = shape[0]
        tmp[2] = shape[2]
        tmp[3] = shape[3]
        tmp[4] = shape[5]
        tmp[5] = shape[1]
        
    if direction == 4:
        
        tmp[0] = shape[1]
        tmp[1] = shape[5]
        tmp[2] = shape[2]
        tmp[3] = shape[3]
        tmp[4] = shape[0]
        tmp[5] = shape[4]

    return tmp

N, M, x, y, K = map(int, input().split())

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

for i in range(K):
    command = commands[i]
    
    if command == 1:

        if y+1 >= M:
            continue
        y += 1
        shape = roll(shape, 1)
    
    elif command == 2:
        
        if y-1 < 0:
            continue
        y -= 1
        shape = roll(shape, 2)
    
    elif command == 3:
        
        if x-1 < 0:
            continue
        x -= 1
        shape = roll(shape, 3)
    
    elif command == 4:
        
        if x+1 >= N:
            continue
        x += 1
        shape = roll(shape, 4)
        
    if maps[x][y] == 0:
        maps[x][y] = dice[shape[5]]
    
    elif maps[x][y] != 0:
        dice[shape[5]] = maps[x][y]
        maps[x][y] = 0
    
    print(dice[shape[0]])