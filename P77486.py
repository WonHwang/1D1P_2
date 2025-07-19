import sys
sys.setrecursionlimit(10**6)

class Seller:
    
    def __init__(self, name, referral):
        self.name = name
        self.referral = referral
        self.amount = 0
    
    def set_money(self, money, sellers):
        up = money//10
        mine = money - up
        self.amount += mine
        if up and self.referral != '-':
            self.up_money(up, sellers)
    
    def up_money(self, money, sellers):
        referral = sellers[self.referral]
        referral.set_money(money, sellers)
    
    def get_amount(self):
        return self.amount

def solution(enroll, referral, seller, amount):
    answer = []
    sellers = dict()
    for i in range(len(enroll)):
        sellers[enroll[i]] = Seller(enroll[i], referral[i])
    for i in range(len(seller)):
        seller_ = seller[i]
        money = amount[i]*100
        seller_ = sellers.get(seller_)
        seller_.set_money(money, sellers)
    for seller_ in enroll:
        answer.append(sellers[seller_].get_amount())
    return answer