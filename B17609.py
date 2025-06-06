import sys
input = sys.stdin.readline
    
for _ in range(int(input())):
    string = input().rstrip()
    cnt = 0
    x, y = 0, len(string)-1
    res = 0
    while x <= y:
        if string[x] != string[y]:
            a, b = x+1, y
            res = 1
            while a <= b:
                if string[a] != string[b]:
                    res = 2
                    break
                a += 1
                b -= 1
            
            if res != 1:
                a, b = x, y-1
                res = 1
                while a <= b:
                    if string[a] != string[b]:
                        res = 2
                        break
                    a += 1
                    b -= 1
            
            if res:
                break
        x += 1
        y -= 1
        
    print(res)