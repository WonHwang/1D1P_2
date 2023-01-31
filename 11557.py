# BOJ 11557번 Yangjojang of The Year

for tc in range(int(input())):
    answer = ""
    Max = "0"
    for n in range(int(input())):
        school, liquar = map(str, input().split())
        if int(liquar) >= int(Max):
            answer, Max = school, liquar
    
    print(answer)