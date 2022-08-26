# 2061번 좋은 암호

primes = [1] * 1000001
primes[0], primes[1] = 0, 0

for i in range(4, 1000001, 2):
    primes[i] = 0

for i in range(3, 1000001, 2):
    if primes[i]:
        for j in range(2*i, 1000001, i):
            primes[j] = 0

K, L = map(int, input().split())

answer = 1
for i in range(2, L):
    if primes[i] and not K%i:
        answer = 0
        break

print('GOOD' if answer else f"BAD {i}")