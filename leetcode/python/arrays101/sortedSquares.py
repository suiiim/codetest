from typing import List

"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""


def sortedSquares(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i] *= nums[i]
    return sorted(nums)


def sortedSquares1(nums: List[int]) -> List[int]:
    startIdx = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            startIdx = i
        nums[i] = nums[i] * nums[i]

    negs = startIdx
    pos = startIdx + 1
    sorted = []

    while pos < len(nums) and negs > -1:
        if nums[negs] <= nums[pos]:
            sorted.append(nums[negs])
            negs -= 1
        elif nums[negs] > nums[pos]:
            sorted.append(nums[pos])
            pos += 1

    while pos < len(nums):
        sorted.append(nums[pos])
        pos += 1

    while negs > -1:
        sorted.append(nums[negs])
        negs -= 1

    return sorted


def sortedSquares2(nums: List[int]) -> List[int]:
    start, end = 0, len(nums) - 1

    sorted_array = []

    while start <= end:
        s = nums[start] ** 2
        e = nums[end] ** 2

        if s > e:
            sorted_array.append(s)
            start += 1

        else:
            sorted_array.append(e)
            end -= 1

    return sorted_array[::-1]


if __name__ == '__main__':
    sortedSquares1([-4, -1, 0, 3, 10])  # [0,1,9,16,100]
    sortedSquares1([-7, -3, 2, 3, 11])  # [4,9,9,49,121]
    sortedSquares2([-4, -1, 0, 3, 10])  # [0,1,9,16,100]
    sortedSquares2([-7, -3, 2, 3, 11])  # [4,9,9,49,121]
