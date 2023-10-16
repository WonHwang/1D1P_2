def solution(n):
    answer = []
    
    primes = [2]
    prime = [1] * 10000
    prime[0], prime[1] = 0, 0
    for i in range(4, 10000, 2):
        prime[i] = 0
    for i in range(3, 10000, 2):
        if prime[i]:
            primes.append(i)
            for j in range(2*i, 10000, i):
                prime[j] = 0
    
    while True:
        if n == 1:
            break
        for p in primes:
            if not n%p:
                answer.append(p)
                while not n%p:
                    n //= p
    
    return answer
