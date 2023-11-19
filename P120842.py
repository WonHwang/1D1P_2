def solution(num_list, n):
    answer = []
    num_list = num_list[::-1]
    while num_list:
        tmp = []
        for _ in range(n):
            tmp.append(num_list.pop())
        answer.append(tmp)
            
    return answer