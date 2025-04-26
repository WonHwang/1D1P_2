months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
string = input().split(", ")
month, day = map(str, string[0].split())
year, time = map(str, string[1].split())
day = int(day)
month = months.get(month)
year = int(year)
hour, minute = map(int, time.split(":"))
yoon = 0

if not year%400 or (not year%4 and year%100):
    yoon = 1

total = 60*24*(365+yoon)

minutes = hour*60 + minute
days = day
for i in range(1, 13):
    if i < month:
        days += date[i]
        if i == 2 and yoon:
            days += 1
days -= 1
minutes += 60*24*days
print(round(100*minutes/total, 10))