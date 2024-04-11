while True:
    line = input()
    if line == "# 0 0":
        break
    name, age, weight = line.split()
    age, weight = int(age), int(weight)

    if age > 17 or weight >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")