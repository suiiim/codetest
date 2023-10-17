from collections import Counter


def solution(participant: list, completion: list):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
