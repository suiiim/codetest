from typing import List

"""Given an array nums of integers, return how many of them contain an even number of digits."""


def findNumbers(nums: List[int]) -> int:
    answer = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            answer += 1
    return answer
