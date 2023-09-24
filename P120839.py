def solution(rsp):
    answer = ''
    res = {
        '2': '0',
        '0': '5',
        '5': '2'
    }
    for digit in rsp:
        answer += res[digit]
    return answer