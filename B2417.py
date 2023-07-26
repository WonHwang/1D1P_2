n = int(input())

left = 0
right = 3100000000

while left < right:
    mid = (left + right) // 2

    if mid ** 2 >= n :
        right = mid
    
    else:
        left = mid + 1

print(right)