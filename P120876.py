def solution(lines):
    answer = 0
    grid = [0] * 201
    for line in lines:
        a, b = line[0], line[1]
        for i in range(a, b):
            grid[i+100] += 1
    for i in range(201):
        if grid[i] >= 2:
            answer += 1
    return answer