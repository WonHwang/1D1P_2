def solution(dartResult):
    answer = []
    for i in range(len(dartResult)):
        digit = dartResult[i]
        if digit == '*':
            x = answer.pop()
            if len(answer) >= 1:
                y = answer.pop()
                answer.append(2*y)
            answer.append(2*x)
        
        elif digit == '#':
            x = answer.pop()
            answer.append(-1*x)
        
        elif digit == 'S' or digit == 'D' or digit == 'T':
            value = int(dartResult[i-1])
            if not value:
                if i-2 >= 0 and dartResult[i-2] == '1':
                    value = 10
            
            if digit == 'S':
                answer.append(value)
            elif digit == 'D':
                answer.append(value**2)
            elif digit == 'T':
                answer.append(value**3)
    
    return sum(answer)