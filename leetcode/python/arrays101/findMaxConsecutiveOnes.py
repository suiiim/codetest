from typing import List

"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    answer = 0
    tmp = 0
    for num in nums:
        if num:
            tmp += 1
        else:
            answer = max(answer, tmp)
            tmp = 0
    return max(answer, tmp)
