dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(command):
    answer = [0, 0]
    direction = 0
    for com in command:
        if com == "R":
            direction += 1
            direction %= 4
        elif com == "L":
            direction -= 1
            direction %= 4
        elif com == "G":
            answer[0] += dx[direction]
            answer[1] += dy[direction]
        else:
            answer[0] -= dx[direction]
            answer[1] -= dy[direction]
    return answer
