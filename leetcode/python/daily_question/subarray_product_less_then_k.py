from typing import List

"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
"""


class Solution:
    # Runtime 3306 ms -> 5.04%
    # Memory 531.66 MB -> 18.30%
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        import bisect

        table = [k]
        total, result = 1, 0

        for n in nums:
            total *= n
            i = bisect.bisect_right(table, total)
            result += len(table[i:])
            table.append(total * k)

        return result

    # Runtime 47 ms -> 87.34%
    # Memory 19.65 MB -> 83.1%
    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        left = 0
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            count += right - left + 1

        return count


a = Solution()
print(a.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))  # 8
print(a.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))  # 0
