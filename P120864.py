def solution(my_string):
    answer = 0
    tmp = "0"
    for digit in my_string:
        if ord("A") <= ord(digit) <= ord("z"):
            answer += int(tmp)
            tmp = "0"
        else:
            tmp += digit
    answer += int(tmp)
    return answer