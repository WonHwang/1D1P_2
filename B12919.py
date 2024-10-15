answer = 0

def dfs(S, T):
    
    global answer
    
    if (not S in T) and (not S in T[::-1]):
        return
    
    if S == T:
        answer = 1
        return
    
    if T and T[-1] == 'A':
        dfs(S, T[:-1])
    
    if T and T[0] == 'B':
        dfs(S, T[::-1][:-1])
        
S = input()
T = input()

dfs(S, T)

print(answer)
