num = input()

step = 0
while True:

    if len(num) == 1:
        answer = 0
        if num == '3' or num == '6' or num == '9':
            answer = 1
        break
    
    sum = 0
    for digit in num:
        sum += int(digit)
    
    num = str(sum)
    step += 1

print(step)
print('YES' if answer else 'NO')