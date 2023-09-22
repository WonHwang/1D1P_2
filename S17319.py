for tc in range(1, int(input())+1):
    
    N = int(input())
    string = input()
    print(f"#{tc} Yes" if not N%2 and string[:N//2] == string[N//2:] else f"#{tc} No")
