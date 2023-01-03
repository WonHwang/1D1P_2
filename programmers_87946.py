# 프로그래머스 87946번 피로도 문제


answer = 0
visited = []

def dfs(t, dungeons, cnt):
    
    global answer
    
    # 매번 방문된 던전 수를 갱신해본다.
    if cnt > answer:
        answer = cnt
    
    # 모든 순서로 던전 입장 테스트해보기
    for i in range(len(dungeons)):
        # 가본적 없는데 갈 수 있으면 간다.
        if not visited[i] and t >= dungeons[i][0]:
            visited[i] = 1
            # 여기는 간걸로 치고 dfs함수 다시 실행 -> 다시 한번 루프를 돈다는 뜻
            dfs(t-dungeons[i][1], dungeons, cnt+1)
            # 안갔다고 생각하고 다음 인덱스의 던전을 보는 것.
            visited[i] = 0

            

def solution(k, dungeons):
    
    global answer, visited
    
    visited = [0] * len(dungeons)
    
    dfs(k, dungeons, 0)
    
    return answer