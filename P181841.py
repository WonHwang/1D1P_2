def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))