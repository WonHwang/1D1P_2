import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = []
for _ in range(N):
    words.append(input().rstrip())
words = list(filter(lambda x:len(x) >= M, words))
words_count = dict()
for word in words:
    words_count[word] = words_count.get(word, 0) + 1
answer = list(set(words))
answer.sort(key=lambda x:(-words_count[x], -len(x), x))
for word in answer:
    print(word)
