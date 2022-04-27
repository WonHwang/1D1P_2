for tc in range(int(input())):
    
    Y, K = 0, 0
    
    for i in range(9):    
        y, k = map(int, input().split())
        Y += y
        K += k
    if Y > K:
        print("Yonsei")
    elif Y == K:
        print("Draw")
    else:
        print("Korea")