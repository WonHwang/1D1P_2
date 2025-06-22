def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    stack = []
    for i in range(N):
        number = numbers[i]
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(i)
    return answer