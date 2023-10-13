def solution(n):
    answer = 0
    
    sieve = [1] * 101
    for i in range(4, 101, 2):
        sieve[i] = 0
    sieve[0] = 0
    sieve[1] = 0
    
    for i in range(3, 101, 2):
        if sieve[i]:
            for j in range(2*i, 101, i):
                sieve[j] = 0
    
    for i in range(2, n+1):
        if not sieve[i]:
            answer += 1
    
    return answer
