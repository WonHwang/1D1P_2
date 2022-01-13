# 1D1P Day3 2057번 팩토리얼 분해

import math

fac = [0] * 20

for i in range(20):
    fac[i] = math.factorial(i)

N = int(input())
answer = []

for i in range(1, (2**20) + 1):
    tmp = bin(i)[2:].zfill(20)
    total = 0

    for j in range(20):
        if int(tmp[j]):
            total += fac[j]
    
    answer.append(total)

print('YES' if N in answer else 'NO')