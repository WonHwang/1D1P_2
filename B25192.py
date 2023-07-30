import sys
input = sys.stdin.readline

N = int(input())

Set = set()
answer = 0

for _ in range(N):
    string = input().rstrip()
    if string == "ENTER":
        Set = set()
    
    elif string not in Set:
        Set.add(string)
        answer += 1

print(answer)