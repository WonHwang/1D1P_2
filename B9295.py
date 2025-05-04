import sys
input = sys.stdin.readline

for tc in range(int(input())):
    print(f"Case {tc+1}: {sum(map(int, input().split()))}")