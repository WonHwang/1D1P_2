# BOJ 2559번 수열 문제

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
start, end = 0, K
Sum = sum(numbers[:K])
Max = Sum
while end < N:
    Sum -= numbers[start]
    Sum += numbers[end]
    start += 1
    end += 1
    if Sum > Max:
        Max = Sum
        
print(Max)