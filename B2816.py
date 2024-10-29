import sys
input = sys.stdin.readline

def swap(idx):
    chs[idx], chs[idx+1] = chs[idx+1], chs[idx]
    
N = int(input())
chs = []
for _ in range(N):
    chs.append(input().rstrip())

answer = ""
idx = 0
state = 0
while True:
    
    if chs[0] == "KBS1" and chs[1] == "KBS2":
        break
    
    if chs[0] != "KBS1":
        if chs[idx] != "KBS1":
            if chs[idx+1] != "KBS1":
                answer += "3"
                swap(idx)
                idx += 1
            else:
                answer += "1"
                idx += 1
        
        elif chs[idx] == "KBS1":
            answer += "4"
            swap(idx-1)
            idx -= 1
    
    elif chs[0] == "KBS1":
        if idx == 0:
            answer += "1"
            idx += 1
        
        elif chs[idx] != "KBS2":
            if chs[idx+1] != "KBS2":
                answer += "3"
                swap(idx)
                idx += 1
            else:
                answer += "1"
                idx += 1
        
        elif chs[idx] == "KBS2":
            answer += "4"
            swap(idx-1)
            idx -= 1        

print(answer)