def solution(nums):
    answer = 0
    N = len(nums) // 2
    nums = set(nums)
    answer = len(nums) if N > len(nums) else N
    return answer
