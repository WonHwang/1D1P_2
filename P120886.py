def solution(before, after):
    return 1 if ''.join(sorted(list(before))) == ''.join(sorted(list(after))) else 0