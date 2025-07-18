import sys
input = sys.stdin.readline

for i in range(1, int(input())+1):
    string = input().rstrip()
    print(f"{i}. {string}")