DP = [i for i in range(50001)]
for i in range(2, int(50001**0.5)+1):
    num = i**2
    for j in range(50001):
        if j+num > 50000:
            break
        
        if DP[j]+1 < DP[j+num]:
            DP[j+num] = DP[j]+1

N = int(input())
print(DP[N])