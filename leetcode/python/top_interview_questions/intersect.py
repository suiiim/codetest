from typing import List

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""


class Solution:
    # Runtime = 95.37%
    # Memory = 60.89%
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        idx1, idx2 = 0, 0
        answer = []
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
            else:
                answer.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
        return answer

    # Memory
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}  # Хеш-таблица для подсчета элементов nums1
        result = []  # Результат
        for nums in nums1:
            if nums in counts:
                counts[nums] += 1
            else:
                counts[nums] = 1
        for i in nums2:
            if i in counts and counts[i] > 0:
                result.append(i)
                counts[i] -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2])  # [2,2]
    s.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])  # [4,9]
