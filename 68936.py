def dfs(x, y, size, arr):
    
    zero, one = 0, 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            if arr[i][j] == 1:
                one += 1
            else:
                zero += 1
    
    if zero == 0:
        return 0, 1
    elif one == 0:
        return 1, 0
    
    res_o, res_z = 0, 0
    a, b = dfs(x, y, size//2, arr)
    res_z += a
    res_o += b
    a, b = dfs(x+(size//2), y, size//2, arr)
    res_z += a
    res_o += b
    a, b = dfs(x, y+(size//2), size//2, arr)
    res_z += a
    res_o += b
    a, b = dfs(x+(size//2), y+(size//2), size//2, arr)
    res_z += a
    res_o += b
    return res_z, res_o

def solution(arr):
    answer = dfs(0, 0, len(arr), arr)
    return answer
