def solution(my_string):
    answer = [0] * 52
    for digit in my_string:
        if ord('A') <= ord(digit) <= ord('Z'):
            answer[ord(digit)-ord('A')] += 1
        elif ord('a') <= ord(digit) <= ord('z'):
            answer[26+ord(digit)-ord('a')] += 1
    return answer
