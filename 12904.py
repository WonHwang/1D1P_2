def solution(s):
    
    for size in range(len(s), -1, -1):
        for i in range(len(s)-size+1):
            tmp = s[i:i+size]
            if tmp == tmp[::-1]:
                return size
