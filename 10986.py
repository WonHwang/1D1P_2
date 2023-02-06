# BOJ 10986번 나머지 합 문제

N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0] * N
prefix_sum += [0]
prefix_sum[0] = nums[0] % M
for i in range(1, N):
    prefix_sum[i] = (prefix_sum[i-1] + nums[i]) % M

rest = [0] * M
rest += [0]
for i in range(N):
    rest[prefix_sum[i]] += 1

answer = rest[0]
for i in range(M):
    answer += rest[i] * (rest[i]-1) // 2

print(answer)