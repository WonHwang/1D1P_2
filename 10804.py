# 1D1P_2 Day1 10804번 카드 역배치

cards = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    target = []
    for i in range(a, b+1):
        target.append(cards[i])

    for i in range(a, b+1):
        cards[i] = target.pop()

print(*cards[1:])