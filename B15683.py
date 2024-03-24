from copy import deepcopy

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

answer = N*M

cameras = []
for i in range(N):
    for j in range(M):
        if grid[i][j] != 0 and grid[i][j] != 6:
            cameras.append((i, j))

def dfs(maps, index, cameras, grid):
    
    global answer
    
    if index >= len(cameras):
        count = count_zeros(maps)
        if count < answer:
            answer = count
        return
    
    x, y = cameras[index][0], cameras[index][1]
    camera = grid[x][y]
    
    if camera == 5:
        new_maps = deepcopy(maps)
        colorize(camera, new_maps, x, y, 0)
        
        dfs(new_maps, index+1, cameras, grid)
    
    if camera == 2:
        for i in range(2):
            new_maps = deepcopy(maps)
            colorize(camera, new_maps, x, y, i)
            
            dfs(new_maps, index+1, cameras, grid)
    
    else:
        for i in range(4):
            new_maps = deepcopy(maps)
            colorize(camera, new_maps, x, y, i)
            
            dfs(new_maps, index+1, cameras, grid)

def count_zeros(maps):
    
    count = 0
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                count += 1
    
    return count
        
def colorize(camera, maps, x, y, direction):
    
    if camera == 5:
        colorize_up(maps, x, y)
        colorize_down(maps, x, y)
        colorize_left(maps, x, y)
        colorize_right(maps, x, y)
        return
    
    if camera == 2:
        if direction == 0:
            colorize_up(maps, x, y)
            colorize_down(maps, x, y)
        else:
            colorize_left(maps, x, y)
            colorize_right(maps, x, y)
        return
    
    if camera == 1:
        if direction == 0:
            colorize_up(maps, x, y)
        elif direction == 1:
            colorize_down(maps, x, y)
        elif direction == 2:
            colorize_left(maps, x, y)
        else:
            colorize_right(maps, x, y)
        return
    
    if camera == 3:
        if direction == 0:
            colorize_up(maps, x, y)
            colorize_right(maps, x, y)
        elif direction == 1:
            colorize_down(maps, x, y)
            colorize_left(maps, x, y)
        elif direction == 2:
            colorize_left(maps, x, y)
            colorize_up(maps, x, y)
        else:
            colorize_right(maps, x, y)
            colorize_down(maps, x, y)
        return
    
    if camera == 4:
        if direction == 0:
            colorize_up(maps, x, y)
            colorize_right(maps, x, y)
            colorize_left(maps, x, y)
        elif direction == 1:
            colorize_down(maps, x, y)
            colorize_right(maps, x, y)
            colorize_left(maps, x, y)
        elif direction == 2:
            colorize_left(maps, x, y)
            colorize_up(maps, x, y)
            colorize_down(maps, x, y)
        else:
            colorize_right(maps, x, y)
            colorize_up(maps, x, y)
            colorize_down(maps, x, y)
        return

def colorize_up(maps, x, y):
    for i in range(N):
        if x-i < 0:
            break
        if maps[x-i][y] == 6:
            break
        if maps[x-i][y] == 0:
            maps[x-i][y] = '#'

def colorize_down(maps, x, y):
    for i in range(N):
        if x+i >= N:
            break
        if maps[x+i][y] == 6:
            break
        if maps[x+i][y] == 0:
            maps[x+i][y] = '#'

def colorize_left(maps, x, y):
    for i in range(M):
        if y-i < 0:
            break
        if maps[x][y-i] == 6:
            break
        if maps[x][y-i] == 0:
            maps[x][y-i] = '#'

def colorize_right(maps, x, y):
    for i in range(M):
        if y+i >= M:
            break
        if maps[x][y+i] == 6:
            break
        if maps[x][y+i] == 0:
            maps[x][y+i] = '#'
            
dfs(grid[::], 0, cameras, grid)

print(answer)