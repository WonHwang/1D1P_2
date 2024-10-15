A = [0]*100
B = [0]*100
for i in range(1, 100):
    A[i] = B[i-1] + (2**(i-1))
    B[i] = B[i-1] + A[i]

def get_number(N):
    
    res = 0
    while N:
        for i in range(100):
            if 2**i <= N < 2**(i+1):
                break
        res += B[i]
        N -= 2**i
        res += N
    return res

x, y = map(int, input().split())
print(get_number(y+1) - get_number(x))
