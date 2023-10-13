def solution(my_string, queries):
    answer = ''
    for query in queries:
        a, b = query[0], query[1]
        my_string = my_string[:a] + my_string[a:b+1][::-1] + my_string[b+1:]
    answer = my_string
    return answer