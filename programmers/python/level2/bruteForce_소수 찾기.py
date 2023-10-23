from itertools import permutations


def solution(numbers):
    def is_prime(number):
        for num in range(2, int(number ** 0.5) + 1):
            if number % num == 0:
                return False
        return True

    def divide_all(number):
        for num in range(2, number):
            if number % num == 0:
                return False
        return True

    answer = []
    for i in range(1, len(numbers) + 1):
        for n in set(map(lambda x: int(''.join(x)), permutations(numbers, i))):
            if n not in (0, 1) and is_prime(n):
                answer.append(n)
    return len(set(answer))


if __name__ == '__main__':
    print(solution("17"))  # 3
    print(solution("011"))  # 2
    print(solution("22"))  # 1
