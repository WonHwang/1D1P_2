import sys
input = sys.stdin.readline

primes = [1] * 1000001
primes[0] = 0
primes[1] = 0

for i in range(4, 1000001, 2):
    primes[i] = 0

for i in range(3, 1000001, 2):
    if primes[i]:
        for j in range(2*i, 1000001, i):
            primes[j] = 0

while True:
    N = int(input())
    
    if not N:
        break
    
    for i in range(3, 1000001, 2):
        if primes[i] and primes[N-i]:
            print(f"{N} = {i} + {N-i}")
            break