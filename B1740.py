N = bin(int(input()))[2:][::-1]
answer = 0
n = 1
for digit in N:
    if digit == "1":
        answer += n
    n *= 3
print(answer)