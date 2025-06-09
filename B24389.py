def reverse(N):
    res = ""
    for digit in N:
        if digit == "1":
            res += "0"
        else:
            res += "1"
    return res

def plusone(N):
    return bin(int("0b" + N, 2) + 1)[2:]

N = bin(int(input()))[2:].zfill(32)
M = plusone(reverse(N))

answer = 0∑
for i in range(32):
    if N[i] != M[i]:
        answer += 1

print(answer)