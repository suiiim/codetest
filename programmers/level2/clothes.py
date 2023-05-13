def solution(clothes: list):
    answer = 1
    collect = dict()
    for v, k in clothes:
        collect.setdefault(k, 1)
        collect[k] += 1
    for i in collect.values():
        answer *= i
    return answer - 1


def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer


if __name__ == '__main__':
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
