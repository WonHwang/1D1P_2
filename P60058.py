def reverse(p):
    
    result = ''
    for d in p:
        if d == '(':
            result += ')'
        else:
            result += '('
    
    return result

def is_balance(p):
    
    cnt, cnt_ = 0, 0
    for d in p:
        if d == '(':
            cnt += 1
        else:
            cnt_ += 1
    
    if cnt == cnt_:
        return True
    
    return False

def is_right(p):
    
    stack = []
    for d in p:
        if d == '(':
            stack.append(d)
        else:
            if not stack:
                return False
            stack.pop()
            
    if stack:
        return False
    
    return True

def transfer(p):
    
    if not p:
        return p
    
    while True:
        if is_right(p):
            return p
        
        u, v = p[:2], p[2:]
        while (not is_balance(u)) and (not is_balance(v)):
            u += v[:2]
            v = v[2:]
        
        if is_right(u):
            return u + transfer(v)
        
        else:
            return '(' + transfer(v) + ')' + reverse(u[1:-1])
    
def solution(p):
    
    answer = transfer(p)
            
    return answer