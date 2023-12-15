dst = {
    "code": 0,
    "date": 1,
    "maximum": 2,
    "remain": 3
}

def solution(data, ext, val_ext, sort_by):
    answer = []
    for d in data:
        if d[dst.get(ext)] < val_ext:
            answer.append(d)
    answer.sort(key = lambda x:x[dst.get(sort_by)])
    return answer