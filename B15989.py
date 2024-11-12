for _ in range(int(input())):
    N = int(input())
    answer = 0
    for i in range(N//3+1):
        n = N - 3*i
        answer += n//2+1
    print(answer)