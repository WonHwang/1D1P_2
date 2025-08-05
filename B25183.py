N = int(input())
string = list(input())
digit = []
for s in string:
    digit.append(ord(s))

answer = "NO"
for i in range(N-4):
    if abs(digit[i]-digit[i+1])==1 and abs(digit[i+1]-digit[i+2])==1 and abs(digit[i+2]-digit[i+3])==1 and abs(digit[i+3]-digit[i+4])==1:
        answer = "YES"
        break
print(answer)