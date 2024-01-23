from typing import List

"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""


class Solution:
    # Runtime = 27.10 %
    # Memory = 70.73 %
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digit = str(int(''.join(map(str, digits))) + 1)
        return [int(num) for num in new_digit]

    # Runtime
    def plusOne1(self, digits: List[int]) -> List[int]:
        carry = 0
        i = len(digits) - 1
        digits[i] += 1
        while i >= 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            i -= 1
            if carry == 0:
                break
        if carry:
            digits.insert(0, carry)
        return digits

    # Memory
    def plusOne2(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits
