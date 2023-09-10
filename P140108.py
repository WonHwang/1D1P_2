def divide(s):

    x = s[0]

    cx, cy = 0, 0
    for i in range(len(s)):
        if s[i] == x:
            cx += 1
        else:
            cy += 1
        
        if cx == cy:
            return s[i+1:]

def solution(s):

    answer = 0

    while s:
        s = divide(s)
        answer += 1
    
    return answer

print(solution("banana")) # 3
print(solution("abracadabra")) # 6
print(solution("aaabbaccccabba")) # 3P