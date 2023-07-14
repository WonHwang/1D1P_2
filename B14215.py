def get_abc(a, b, c):
    tmp = [a, b, c]
    tmp.sort()
    return tmp[0], tmp[1], tmp[2]

a, b, c = map(int, input().split())

while True:

    a, b, c = get_abc(a, b, c)

    if a + b > c:
        print(a+b+c)
        break

    c -= 1