A, B = map(int, input().split())
N, M = map(int, input().split())
robots = {i: [] for i in range(1, N+1)}
maps = [[0 for _ in range(B)] for _ in range(A)]
for i in range(1, N+1):
    x, y, d = map(str, input().split())
    x, y = int(x)-1, int(y)-1
    robots[i] = [x, y, d]
    maps[x][y] = i

commands = []
for _ in range(M):
    commands.append(input())

for c in range(M):
    
    
    robot, command, repeat = map(str, commands[c].split())
    robot, repeat = int(robot), int(repeat)
    
    error_occured = 0
    for __ in range(repeat):
        info = robots[robot]
        x, y, d = info[0], info[1], info[2]
        
        if command == 'L':
            if d == 'N':
                d = 'W'
            elif d == 'W':
                d = 'S'
            elif d == 'S':
                d = 'E'
            elif d == 'E':
                d = 'N'
            
            robots[robot] = [x, y, d]
        
        elif command == 'R':
            if d == 'N':
                d = 'E'
            elif d == 'E':
                d = 'S'
            elif d == 'S':
                d = 'W'
            elif d == 'W':
                d = 'N'
            
            robots[robot] = [x, y, d]
        
        elif command == 'F':
            if d == 'N':
                x_, y_ = x, y+1
            elif d == 'W':
                x_, y_ = x-1, y
            elif d == 'S':
                x_, y_ = x, y-1
            else:
                x_, y_ = x+1, y
            
            if x_ < 0 or x_ == A or y_ < 0 or y_ == B:
                error_occured = 1
                print(f"Robot {robot} crashes into the wall")
                break
            elif maps[x_][y_]:
                error_occured = 1
                print(f"Robot {robot} crashes into robot {maps[x_][y_]}")
                break
            else:
                maps[x][y] = 0
                maps[x_][y_] = robot
                robots[robot] = [x_, y_, d]
    if error_occured:
        break

if not error_occured:
    print('OK')