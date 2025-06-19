num = input()
size = len(num)
answer = ""
half = size//2
if size%2:
    tmp = num[:half+1]
    f = tmp + tmp[::-1][1:]
else:
    tmp = num[:half]
    f= tmp + tmp[::-1]
answer = f
if int(f) <= int(num):
    tmp = str(int(tmp)+1)
    if size%2:
        answer = tmp + tmp[::-1][1:]
    else:
        answer = tmp + tmp[::-1]
    if size%2 and len(tmp) > half+1:
        answer = int(num)+2
    elif not size%2 and len(tmp) > half:
        answer = int(num)+2
print(answer)