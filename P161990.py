def solution(wallpaper):
    l, t = 50, 50
    r, b = 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                if i < t:
                    t = i
                if i > b:
                    b = i
                if j < l:
                    l = j
                if j > r:
                    r = j
    return [t, l, b+1, r+1]
