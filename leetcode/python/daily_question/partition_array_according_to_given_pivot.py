from typing import List

"""
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained. 
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. 
If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
Return nums after the rearrangement.
"""


class Solution:
    # Runtime 32 ms -> 57.48%
    # Memory 35.45 MB -> 20.61%
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [pivot] * len(nums)
        left, right = 0, -1

        for i in nums:
            if i < pivot:
                result[left] = i
                left += 1
            elif i > pivot:
                result[right] = i
                right -= 1

        if right != -1:
            result[right + 1:] = result[right + 1:][::-1]

        return result

    # Runtime 27 ms -> 77.27%
    # Memory 35.65 MB -> 5.30%
    def pivotArray2(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        big = []
        c = 0
        for i in nums:
            if i < pivot:
                small.append(i)
            elif i > pivot:
                big.append(i)
            elif i == pivot:
                c += 1
        res = []
        res += small
        res += [pivot] * c
        res += big
        return res

    # Runtime 41 ms -> 35.81%
    # Memory 32.57 MB -> 100%
    def pivotArray3(self, nums: List[int], pivot: int) -> List[int]:
        n = nums.copy()
        nums.clear()
        less, piv, gre = [], [], []
        for i in n:
            if i < pivot:
                less.append(i)
            if i == pivot:
                piv.append(i)
            if i > pivot:
                gre.append(i)
        nums = [*less, *piv, *gre]
        return nums


a = Solution()
print(a.pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10))  # [9,5,3,10,10,12,14]
print(a.pivotArray(nums=[-3, 4, 3, 2], pivot=2))  # [-3,2,4,3]
