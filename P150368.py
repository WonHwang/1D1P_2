rates = [40, 30, 20, 10]
cnt = 0
total = 0

def dfs(idx, rate, users, emoticons):
    
    global cnt, total
    
    if idx == len(emoticons):
        res, price = 0, 0
        for user in users:
            tmp = 0
            r, maximum = user[0], user[1]
            for i in range(len(emoticons)):
                if rate[i] >= r:
                    tmp += emoticons[i] * (100-rate[i]) // 100
            if tmp >= maximum:
                res += 1
            else:
                price += tmp
        
        if res > cnt:
            cnt = res
            total = price
        
        elif res == cnt and price > total:
            total = price
        
        return
    
    for i in range(4):
        rate.append(rates[i])
        dfs(idx+1, rate, users, emoticons)
        rate.pop()

def solution(users, emoticons):
    dfs(0, [], users, emoticons)
    return [cnt, total]