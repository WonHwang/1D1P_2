# programmers 17686번 파일명 정렬 문제

def solution(files):

    splited_files = []
    for file in files:
        start = 0
        end = 0
        for i in range(len(file)):
            if not start and ord('0') <= ord(file[i]) <= ord('9'):
                start = i
            if start and not (ord('0') <= ord(file[i]) <= ord('9')):
                end = i
                break
        if not end:
            end = len(file)
        
        splited_files.append({
            "original": file[:start],
            "number": int(file[start:end]),
            "tail": file[end:],
            "lower": file[:start].lower(),
            "original_number": file[start:end]
        })
    splited_files.sort(key=lambda x:(x["lower"], x["number"]))
    answer = []
    for file in splited_files:
        answer.append(file["original"]+file["original_number"]+file["tail"])

    return answer