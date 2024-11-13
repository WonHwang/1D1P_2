def get_count(word):
    cnt = [0] * 26
    for digit in word:
        cnt[ord(digit)-65] += 1
    return cnt

N = int(input())
word = sorted(list(input()))
answer = 0
for _ in range(N-1):
    target = sorted(list(input()))
    if len(word) == len(target):
        if ''.join(word) == ''.join(target):
            answer += 1
            continue
        res = 0
        cnt = get_count(word)
        cnt_ = get_count(target)
        for i in range(26):
            res += abs(cnt[i]-cnt_[i])
        if res <= 2:
            answer += 1
    elif len(word) > len(target):
        if ''.join(word[:-1]) == ''.join(target):
            answer += 1
            continue
        for i in range(len(target)):
            if word[i] != target[i]:
                if ''.join(word) == ''.join(target[:i] + [word[i]] + target[i:]):
                    answer += 1
    elif len(target) > len(word):
        if ''.join(target[:-1]) == ''.join(word):
            answer += 1
            continue
        for i in range(len(word)):
            if word[i] != target[i]:
                if ''.join(target) == ''.join(word[:i] + [target[i]] + word[i:]):
                    answer += 1
print(answer)

'''
10
ABABA
BBAAC
BBAAD
BBAAE
BBAAB
ACQAC
LKJDS
OKWLN
OKNLS
PONLM
'''