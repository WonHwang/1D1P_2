def solution(my_string, num1, num2):
    return ''.join(list(my_string[:num1]) + [my_string[num2]] + list(my_string[num1+1:num2]) + [my_string[num1]] + list(my_string[num2+1:]))