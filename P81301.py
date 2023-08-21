dictionary = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def solution(s):
    answer = ""
    idx = 0
    tmp = ""
    
    while idx < len(s):
        
        if '0' <= s[idx] <= '9':
            answer += s[idx]
            idx += 1
        else:
            tmp += s[idx]
            idx += 1
            
            if dictionary.get(tmp):
                answer += dictionary.get(tmp)
                tmp = ""
    
    return int(answer)