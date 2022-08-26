# 1D1P Day6 1418번 K-세준수

sieve = [1] * 50001
sieve[0], sieve[1] = 0, 0

for i in range(4, 50001, 2):
    sieve[i] = 0

for i in range(3, 50001, 2):
    if sieve[i]:
        for j in range(2*i, 50001, i):
            sieve[j] = 0

primes = []
primes.append(2)
for i in range(3, 50001, 2):
    if sieve[i]:
        primes.append(i)

N = int(input())
K = int(input())

divider = [i for i in range(N+1)]

for prime in primes:
    for i in range((N // prime) + 1):
        divider[prime * i] = prime

answer = 0
for i in range(1, N+1):
    if divider[i] <= K:
        answer += 1

print(answer)