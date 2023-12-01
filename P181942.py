def solution(str1, str2):
    answer = ''
    for i in range(2*len(str1)):
        answer += str2[i//2] if i%2 else str1[i//2]
            
    return answer
