N = int(input())
score = [[0, 0, 0, 0, 1], [0, 0, 0, 0, 2], [0, 0, 0, 0, 3]]
for _ in range(N):
    nums = list(map(int, input().split()))
    for i in range(3):
        num = nums[i]
        score[i][0] += num
        score[i][num] += 1

score.sort(key=lambda x:(x[0], x[1], x[2]), reverse=True)
if score[0][0] > score[1][0]:
    print(score[0][4], score[0][0])

elif score[0][0] == score[1][0]:
    if score[0][1] > score[1][1]:
        print(score[0][4], score[0][0])
    
    elif score[0][1] == score[1][1]:
        if score[0][2] > score[1][2]:
            print(score[0][4], score[0][0])
        
        elif score[0][2] == score[1][2]:
            print(0, score[0][0])