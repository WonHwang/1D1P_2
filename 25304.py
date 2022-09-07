X = int(input())
N = int(input())
for _ in range(N):
    price, many = map(int, input().split())
    X -= price * many

if X:
    print("No")
else:
    print("Yes")