word2 = ["ye", "ma"]
word3 = ["aya", "woo"]

def solution(babbling):
    
    answer = 0
    
    for word in babbling:
        past = ""
        result = 1
        
        while word:
            if len(word) < 2:
                result = 0
                break
            
            if word[:2] in word2:
                if word[:2] == past:
                    result = 0
                    break
                past = word[:2]
                word = word[2:]
                continue
            
            if len(word) < 3:
                result = 0
                break
            
            if word[:3] in word3:
                if word[:3] == past:
                    result = 0
                    break
                past = word[:3]
                word = word[3:]
                continue
            
            result = 0
            break
            
        if result:
            answer += 1
            
    return answer