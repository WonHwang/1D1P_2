from itertools import permutations

N, K = map(int, input().split())
kits = list(map(int, input().split()))

answer = 0
for p in permutations(kits):
    score = 500
    for kit in p:
        score -= K
        score += kit

        if score < 500:
            break
    
    if score >= 500:
        answer += 1

print(answer)