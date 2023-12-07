def solution(n):
    answer = []
    for i in range(1, int(n**0.5)+1):
        if not n%i:
            answer.append(i)
            if n//i not in answer:
                answer.append(n//i)
    return sorted(answer)
