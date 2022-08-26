def solution(id_list, report, k):

    members = dict()
    report_list = dict()
    for id in id_list:
        members[id] = set()
        report_list[id] = set()
    
    for rep in report:
        members[rep[1]].add(rep[0])
        report_list[rep[0]].add(rep[1])

    answer = []

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))