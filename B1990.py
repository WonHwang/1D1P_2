def is_primes(n):

    if not n:
        return False
    
    if n == 1:
        return False
    
    if n == 2:
        return True
    
    if not n%2:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if not n%i:
            return False
    
    return True

a, b = map(int, input().split())

res = set()
def dfs(n):

    num = int(n)
    
    if num > b or len(n) > 8:
        return
    
    if a <= num <= b and is_primes(num) and not num in res:
        res.add(num)
    
    for i in range(10):
        tmp = str(i)+ n +str(i)
        dfs(tmp)

for i in range(10):
    dfs(str(i))
dfs("11")

res = list(res)
res.sort()
res.append(-1)
for num in res:
    print(num)