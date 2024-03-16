def check(string):
    
    if string != string[::-1]:
        return False
    
    length = len(string)
    if string[:length//2] != string[:length//2][::-1]:
        return False
    
    if string[:-length//2:-1] != string[:-length//2:-1][::-1]:
        return False
    
    return True

for tc in range(1, int(input())+1):
    
    string = input()
    
    print(f"#{tc} YES" if check(string) else f"#{tc} NO")