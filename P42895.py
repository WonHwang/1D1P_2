def solution(N, number):
    M = 32001
    dp = dict()
    for i in range(1, 9):
        dp[int(str(N)*i)] = i
    for _ in range(8):
        nums = list(dp.keys())
        for a in nums:
            for b in nums:
                cnt = dp[a] + dp[b]
                if cnt < 9:
                    num = a+b
                    if num < M:
                        if dp.get(num):
                            dp[num] = min(dp.get(num), cnt)
                        else:
                            dp[num] = cnt
                    
                    num = abs(a-b)
                    if dp.get(num):
                        dp[num] = min(dp.get(num), cnt)
                    else:
                        dp[num] = cnt
                    
                    num = a*b
                    if num < M:
                        if dp.get(num):
                            dp[num] = min(dp.get(num), cnt)
                        else:
                            dp[num] = cnt
                    
                    if b and not a%b:
                        num = a//b
                        if dp.get(num):
                            dp[num] = min(dp.get(num), cnt)
                        else:
                            dp[num] = cnt
                    
                    if a and not b%a:
                        num = b//a
                        if dp.get(num):
                            dp[num] = min(dp.get(num), cnt)
                        else:
                            dp[num] = cnt
    
    return dp.get(number, -1)