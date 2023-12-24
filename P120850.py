def solution(my_string):
    return sorted(list(map(int, filter(lambda x: ord('0') <= ord(x) <= ord('9'), my_string))))