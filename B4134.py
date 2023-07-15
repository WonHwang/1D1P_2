def isprime(N):

    if N == 1:
        return False
    
    if N == 2:
        return True

    if not N%2:
        return False

    for i in range(3, int(N**0.5)+1, 2):
        if not N%i:
            return False
    
    return True

for _ in range(int(input())):
    N = int(input())
    while True:
        if isprime(N):
            print(N)
            break
        N += 1