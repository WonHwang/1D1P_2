def solution(number, k):
    number = list(number)
    stack = []
    for num in number:
        if not stack:
            stack.append(num)
            continue
        
        while stack and k and stack[-1] < num:
            stack.pop()
            k -= 1
        
        stack.append(num)
    if k:
        stack.pop()
    return ''.join(stack)