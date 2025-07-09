import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if not N:
        break
    strings = []
    dic = dict()
    for _ in range(N):
        string = input().rstrip()
        dic[string.lower()] = string
        strings.append(string.lower())
    strings.sort()
    print(dic.get(strings[0]))