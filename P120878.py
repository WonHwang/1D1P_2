def solution(a, b):
    answer = 1
    for i in range(2, 1001):
        if (not a%i) and (not b%i):
            while True:
                if a%i or b%i:
                    break
                a //= i
                b //= i
    
    if b == 1:
        return 1
    
    div = []
    for i in range(2, b+1):
        if not b%i:
            while True:
                if b%i:
                    break
                div.append(i)
                b //= i
    
    for num in div:
        if num != 2 and num != 5:
            answer = 2
            break
    
    return answer
