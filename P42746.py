
import functools import cmp_to_key

def compare(a, b):
    
    tmp1, tmp2 = int(a+b), int(b+a)
    
    if tmp1 < tmp2:
        return 1
    
    elif tmp1 == tmp2:
        return 0
    
    else:
        return -1

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    answer = ''.join(numbers)
    if int(answer) == 0:
        answer = "0"
    return answer
