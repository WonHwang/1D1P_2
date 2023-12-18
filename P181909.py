def solution(my_string):
    return sorted([my_string[::-1][:i][::-1] for i in range(1, len(my_string)+1)])
