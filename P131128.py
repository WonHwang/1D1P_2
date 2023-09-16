def solution(X, Y):
    answer = ""
    X_dict = dict()
    Y_dict = dict()
    for i in range(10):
        X_dict[str(i)] = 0
        Y_dict[str(i)] = 0
    for x in X:
        X_dict[x] += 1
    for y in Y:
        Y_dict[y] += 1
    
    for i in range(9, -1, -1):
        target = str(i)
        tmp = min(X_dict[target], Y_dict[target])
        for _ in range(tmp):
            answer += target
    
    if not answer:
        answer = "-1"
    
    if answer and answer[0] == "0" and answer[-1] == "0":
        answer = "0"
    
    return answer