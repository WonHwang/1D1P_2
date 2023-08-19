def solution(s, n):
    answer = ''
    for a in s:
        if ord('a') <= ord(a) <= ord('z'):
            answer += chr((ord(a) - ord('a') + n) % 26 + ord('a'))
        elif ord('A') <= ord(a) <= ord('Z'):
            answer += chr((ord(a) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += " "
    return answer