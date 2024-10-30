import sys
input = sys.stdin.readline

vowel = ('a', 'e', 'i', 'o', 'u')

while True:
    word = input().rstrip()
    if word == "end":
        break
    
    flag = False
    for char in word:
        if char in vowel:
            flag = True
            break
    
    if not flag:
        print(f"<{word}> is not acceptable.")
        continue
    
    flag = True
    for i in range(len(word)-2):
        if word[i] in vowel and word[i+1] in vowel and word[i+2] in vowel:
            flag = False
            break
        if word[i] not in vowel and word[i+1] not in vowel and word[i+2] not in vowel:
            flag = False
            break
    
    if not flag:
        print(f"<{word}> is not acceptable.")
        continue
    
    flag = True
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            if not ((word[i] == "e" and word[i+1] == "e") or (word[i] == "o" and word[i+1] == "o")):
                flag = False
                break
    
    if not flag:
        print(f"<{word}> is not acceptable.")
        continue
    
    print(f"<{word}> is acceptable.")
