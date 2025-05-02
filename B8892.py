import sys
input = sys.stdin.readline

def is_pal(word):
    N = len(word)
    i, j = 0, N-1
    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    
    return True

for tc in range(int(input())):
    k = int(input())
    words = []
    for _ in range(k):
        words.append(input().rstrip())
    
    answer = 0
    for i in range(k):
        a = words[i]
        for j in range(i+1, k):
            b = words[j]
            if is_pal(a+b):
                answer = a+b
                break
            if is_pal(b+a):
                answer = b+a
                break
        if answer:
            break
        
    print(answer)