def solution(myString):
    answer = ''
    for digit in myString:
        if ord(digit) < ord('l'):
            answer += 'l'
        else:
            answer += digit
    return answer