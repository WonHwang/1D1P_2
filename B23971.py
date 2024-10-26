H, W, N, M = map(int, input().split())
print((H//(N+1) if not H%(N+1) else (H//(N+1))+1) * (W//(M+1) if not W%(M+1) else (W//(M+1))+1))