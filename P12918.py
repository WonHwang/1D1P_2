def solution(s):
    
    if not len(s) in [4, 6]:
        return False
    
    for char in s:
        if not (ord('0') <= ord(char) <= ord('9')):
            return False
    
    return True