solution=lambda x,y:[a+[y,0][i%2] if len(x)%2 else a+[0,y][i%2] for i,a in enumerate(x)]