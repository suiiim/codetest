from collections import Counter


def solution1(nums: list):
    answer = 0
    c = Counter(nums)
    return int(len(nums) / 2) if len(nums) / 2 <= len(c) else len(c)


def solution2(ls):
    return min(len(ls) / 2, len(set(ls)))


if __name__ == '__main__':
    print(solution1([3, 1, 2, 3]))
    print(solution1([3, 3, 3, 2, 2, 4]))
    print(solution1([3, 3, 3, 2, 2, 2]))

    print(solution2([3, 1, 2, 3]))
    print(solution2([3, 3, 3, 2, 2, 4]))
    print(solution2([3, 3, 3, 2, 2, 2]))
