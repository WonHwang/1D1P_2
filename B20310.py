string = input()
one, zero = string.count('1'), string.count('0')
string = list(string)
cnt = one // 2
for i in range(len(string)):
    if cnt and string[i] == '1':
        string[i] = ''
        cnt -= 1

cnt = zero // 2
for i in range(len(string)-1, -1, -1):
    if cnt and string[i] == '0':
        string[i] = ''
        cnt -= 1

string = ''.join(string)
print(string)