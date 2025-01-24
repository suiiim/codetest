from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    # Runtime 890 ms -> 22.89%
    # Memory 20.69 MB -> 51.46%
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums = sorted(nums)
        last = nums.index(0) + 1 if 0 in nums else len(nums) - 2

        tmp = 10 ** 5
        for i in range(last):
            if nums[i] == tmp:
                continue
            s = i + 1
            e = len(nums) - 1
            tmp = nums[i]
            while s < e:
                num = tmp + nums[s] + nums[e]
                if num == 0:
                    result.append([tmp, nums[s], nums[e]])

                if num <= 0:
                    origin = nums[s]
                    while origin == nums[s]:
                        s += 1
                        if s > last:
                            break
                if num >= 0:
                    origin = nums[e]
                    while origin == nums[e]:
                        e -= 1
                        if e < 2:
                            break

        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        from bisect import bisect_right

        nums.sort()
        index = 1
        x = nums[0]
        counter = 1
        # 값이 3개 이상 있는 경우는 삭제하기
        while index < len(nums):
            if nums[index] == x:
                counter = counter + 1
                if x == 0:
                    if counter > 3:
                        nums.pop(index)
                    else:
                        index = index + 1
                elif counter > 2:
                    nums.pop(index)
                else:
                    index = index + 1
            else:
                x = nums[index]
                counter = 1
                index = index + 1
        if not all(n > 0 for n in nums):
            counts = Counter(nums)
            result = [[0, 0, 0]] if counts[0] >= 3 else []
            nums = [i for i in sorted(counts) if i != 0]
            # 0을 포함한 +- 둘 다 있는 숫자 찾기
            if counts[0] > 0:
                for i in nums:
                    if i > 0:
                        break
                    if -i in counts:
                        result.append([-i, 0, i])
            # 특정값이 2개 이상 있는 숫자 찾기
            for i in nums:
                if i & 1:
                    continue
                remaining = -i >> 1
                if counts[remaining] >= 2:
                    result.append([i, remaining, remaining])
            for i, n in enumerate(nums):
                kk = -(nums[0] + n)
                if kk < n:
                    break
                j = bisect_right(nums, -n << 1) if n < 0 else i + 1
                k = bisect_right(nums, kk)
                for right in nums[j:k]:
                    left = -(n + right)
                    if left in counts:
                        result.append([left, n, right])
            del counts, nums
            return result
        else:
            return []

    def threeSum3(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        if (nums[-1] < 0) or (nums[0] > 0):
            return []

        triplets = []
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            elif nums[left] > 0:
                break

            else:
                target = -nums[left]
                middle = left + 1
                right = len(nums) - 1

                while middle < right:
                    total = nums[middle] + nums[right]

                    if total < target:
                        middle += 1

                    elif total > target:
                        right -= 1

                    else:
                        triplets.append([nums[left], nums[middle], nums[right]])

                        middle += 1
                        right -= 1

                        while middle < right and nums[middle] == nums[middle - 1]:
                            middle += 1

        return triplets


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))  # []
print(a.threeSum([0, 0, 0]))  # [[0,0,0]]
print(a.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
print(a.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(a.threeSum([-2, 0, 1, 1, 2]))  # [[-2,0,2],[-2,1,1]]
print(a.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(a.threeSum([0, 1, 1]))  # []
