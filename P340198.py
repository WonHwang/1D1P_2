def is_possible(mat, park):
    N = len(park)
    M = len(park[0])
    
    for i in range(N-mat+1):
        for j in range(M-mat+1):
            if park[i][j] == '-1':
                res = True
                for x in range(mat):
                    for y in range(mat):
                        if park[i+x][j+y] != '-1':
                            res = False
                            break
                    if not res:
                        break
                if res:
                    return True
    return False
                

def solution(mats, park):
    answer = 0
    for mat in mats:
        if is_possible(mat, park):
            if mat > answer:
                answer = mat
    return answer if answer else -1