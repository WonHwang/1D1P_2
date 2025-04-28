'''
O(g(n)) = {f(n) | 모든 n >= n0에 대해서 f(n) <= c x g(n) 인 양의 상수 c와 n0가 존재한다}
f(n) = a1 x n + a0, 양의 정수 c, n가 주어질때 O(n)의 정의를 만족하는지 알아보자.

a1, a0, c, n0가 주어졌을 때 정의를 만족하는지 파악해보자

ex1)
7 7
8
1

ans1)
0

a1 = 7, a0 = 7, c = 8, n0 = 1이다.
f(n) = 7n + 7, n >= 1 에 대해서 f(n) = 7n + 7 <= 8 x n 인가? => n=1 이면 14 <= 8 (x)

'''

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

answer = 1
for i in range(n0, 10000):
    if a1*i + a0 > c*i:
        answer = 0
        break

print(answer)