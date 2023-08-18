for _ in range(int(input())):

    string = ""
    while True:
        tmp = input()
        if tmp == "":
            break
        string += tmp
    
    total = 0
    cnt = 0
    for digit in string:
        total += 1
        if digit == "#":
            cnt += 1
    
    answer = round(round((total - cnt) / total, 3) * 100, 1)

    if answer == int(answer):
        answer = int(answer)

    print(f"Efficiency ratio is {answer}%.")