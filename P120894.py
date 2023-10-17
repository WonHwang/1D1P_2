x={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
def solution(numbers):
    answer = ""
    numbers = list(numbers[::-1])
    tmp = ""
    while numbers:
        tmp += numbers.pop()
        if tmp in x:
            answer += x[tmp]
            tmp = ""
    return int(answer)
