def solution(s):
    answer = [-1] * len(s)
    for c in range(ord('a'), ord('z')+1):
        char = chr(c)
        idx = -1
        for i in range(len(s)):
            if char == s[i]:
                if idx == -1:
                    idx = i
                else:
                    answer[i] = i - idx
                    idx = i
    return answer
