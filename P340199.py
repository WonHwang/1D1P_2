def solution(wallet, bill):
    answer = 0
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        bill = [max(bill)//2, min(bill)]
        answer += 1
    return answer