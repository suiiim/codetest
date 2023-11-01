def solution(people, limit):
    answer = 0
    # 두 포인터
    start, end = 0, len(people) - 1
    people.sort()
    while True:
        # 최대 수용 인원 = 2명
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
        if start > end:
            break
    return answer


if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))  # 3
    print(solution([70, 80, 50], 100))  # 3
