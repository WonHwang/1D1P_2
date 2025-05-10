N, M = map(int, input().split())

Six, One = 1000, 1000
for _ in range(M):
    six, one = map(int, input().split())
    if six < Six:
        Six = six
    if one < One:
        One = one

answer = 0
if One*6 > Six:
    answer = Six*(N//6)
    answer += One*(N%6) if One*(N%6) < Six else Six
else:
    answer = One*N

print(answer)