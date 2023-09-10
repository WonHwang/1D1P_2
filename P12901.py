from datetime import datetime
def solution(a, b):
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    current = datetime(2016, 1, 1)
    future = datetime(2016, a, b)
    
    if future == current:
        return "FRI"
    
    period = future - current

    listing = list(str(period).strip().split(','))
    days = list(listing[0].strip().split(' '))
    return weeks[int(days[0]) % 7]