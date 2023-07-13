while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    tmp = [a, b, c]
    tmp.sort()
    a, b, c = tmp[0], tmp[1], tmp[2]

    if a + b <= c:
        print("Invalid")
        continue

    if a == b and b == c and c == a:
        print("Equilateral")
        continue

    if a == b or b == c or c == a:
        print("Isosceles")
        continue

    print("Scalene")