A, B = map(int, input().split())
N = 10000001
primes = [1] * N
primes[0] = 0
primes[1] = 0
for i in range(4, N, 2):
    primes[i] = 0
for i in range(3, N, 2):
    if primes[i]:
        for j in range(2*i, N, i):
            primes[j] = 0
prime = [2]
for i in range(3, N, 2):
    if primes[i]:
        prime.append(i)

answer = 0
for num in prime:
    if num**2 > B:
        break
    for i in range(2, N):
        if A <= num**i <= B:
            answer += 1
        elif num**i > B:
            break
        
print(answer)