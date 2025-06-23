def gcd(a, b):
    if b > a:
        a, b = b, a
    
    while b:
        a, b = b, a%b
    
    return a

def solution(weights):
    target = [2, 3, 4]
    answer = 0
    cand = dict()
    for weight in weights:
        cand[weight] = cand.get(weight, 0) + 1
    
    weights = []
    for key in cand:
        weights.append(key)
    size = len(weights)
    
    for x in range(size):
        for y in range(x, size):
            a, b = weights[x], weights[y]
            if a == b:
                answer += cand[a]*(cand[a]-1)//2
            else:
                for i in target:
                    for j in target:
                        if a*i == b*j:
                            answer += cand[a]*cand[b]
    return answer