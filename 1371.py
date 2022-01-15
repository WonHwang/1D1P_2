# 1D1P Day5 1371번 가장 많은 글자

count = [0] * 26

while True:
    try:
        line = input()
        for digit in line:
            if digit != ' ':
                count[ord(digit)-ord('a')] += 1
    
    except:
        break

answer = ''
Max = max(count)
for i in range(26):
    if count[i] == Max:
        answer += chr(i + ord('a'))

print(answer)