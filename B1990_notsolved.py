def is_primes(n):

    if not n%2:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if not n%i:
            return False
    
    return True

a, b = map(int, input().split())
res = []

def dfs(n):

    if n > b:
        return
    
    if a <= n <= b and is_primes(n):
        res.append(n)
    
    for i in range(1, 10, 2):
        dfs(int(str(i)+str(n)+str(i)))

for i in range(10):
    dfs(i)

for i in range(11, 100, 11):
    dfs(i)

res.sort()
for num in res:
    print(num)
print(-1)