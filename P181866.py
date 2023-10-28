def solution(myString):
    answer = []
    word = ""
    for digit in myString:
        if digit == "x":
            if word:
                answer.append(word)
                word = ""
            continue
        
        word += digit
    
    if word:
        answer.append(word)
    
    return sorted(answer)