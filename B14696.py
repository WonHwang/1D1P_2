import sys
input = sys.stdin.readline

for r in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    A = [0] * 5
    B = [0] * 5
    
    for i in range(1, len(a)):
        A[a[i]] += 1
    for i in range(1, len(b)):
        B[b[i]] += 1
    
    for i in range(4, 0, -1):
        if A[i] > B[i]:
            print("A")
            break
        elif A[i] < B[i]:
            print("B")
            break
    else:
        print("D")