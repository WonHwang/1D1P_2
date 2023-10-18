def solution(spell, dic):
    answer = 2
    spell = ''.join(sorted(spell))
    for d in dic:
        if ''.join(sorted(d)) == spell:
            answer = 1
            break
    return answer
