import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(str, input().rstrip().split())
    print(bin(int("0b" + A, 2) + int("0b" + B, 2))[2:])