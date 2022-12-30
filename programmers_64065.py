# 프로그래머스 64065번 튜플 문제

def solution(s):
    answer = []

    # 제일 앞,뒤 중괄호 제거, 각 튜플 간 },{ 제거
    s = "".join(list(s)[1:-1]).split('},{')

    # 첫번째 원소와 마지막 원소는 각각 {, }가 아직 붙어 있다. 제거하자.
    s[0] = s[0][1:]
    s[-1] = s[-1][:-1]
    
    to_list = []
    for l in s:
        # 각 l들은 1,2,3 형태의 문자열이므로 split해서 set형태로 넣어준다
        to_list.append(set(map(int, l.split(','))))
    
    # 순서대로 뭐가 추가 되었는지 확인하기 위해서 원소 개수 기준으로 정렬
    to_list.sort(key=lambda x:len(x))

    # 첫번째꺼는 차집합 할 대상이 없으므로 미리 넣어두고
    answer.append(list(to_list[0]).pop())
    for i in range(len(to_list)-1):
        # 두번째꺼 부터는 차집합해서 뭐가 추가되었는지 표기
        target = list(to_list[i+1].difference(to_list[i]))[0]
        answer.append(target)
    return answer