def solution(keymap, targets):
    answer = []
    key_map = dict()
    for target in targets:
        for digit in target:
            if digit in key_map:
                continue
            cnt = []
            for key in keymap:
                if digit in key:
                    cnt.append(key.index(digit)+1)
            if cnt:
                res = min(cnt)
            else:
                res = -1
            key_map[digit] = res
    
    for target in targets:
        cnt = 0
        for digit in target:
            res = key_map[digit]
            if res == -1:
                cnt = -1
                break
            else:
                cnt += res
        answer.append(cnt)
        
    return answer