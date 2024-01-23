from typing import List

"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""


class Solution:
    # Runtime = 64.37 %
    # Memory = 13.70 %
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        return False if len(c) == len(nums) else True

    # Runtime = 85.91 %
    # Memory = 63.94 %
    def containsDuplicate1(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True

    # Runtime = 93.95 %
    # Memory = 63.94 %
    def containsDuplicate2(self, nums: List[int]) -> bool:
        # brute force would be a double loop
        dictionary = set()
        for num in nums:
            if num in dictionary:
                return True
            dictionary.add(num)
        return False

    # Runtime = 54.89%
    # Memory = 99.83%
    def containsDuplicate3(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        prev_num: int = nums[0]
        for i in range(1, len(nums)):
            if prev_num == nums[i]:
                return True

            prev_num = nums[i]

        return False


if __name__ == '__main__':
    s = Solution()
    s.containsDuplicate([1, 2, 3, 1])  # true
    s.containsDuplicate([1, 2, 3, 4])  # false
    s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])  # true
