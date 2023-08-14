def solution(s):
    arr = list(map(str, s.split()))
    result = []
    for word in arr:
        tmp = ""
        for i in range(len(word)):
            if not i%2:
                tmp += word[i].upper()
            else:
                tmp += word[i].lower()
        result.append(tmp)
        
    result = result[::-1]
    answer = ""
    i = 0
    
    while i < len(s):
        if s[i] == " ":
            answer += " "
        else:
            tmp = result.pop()
            i += len(tmp)
            answer += tmp
            continue
        i += 1
    
    return answer

s = "try hello world"
print(solution(s))