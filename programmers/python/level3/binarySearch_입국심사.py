def solution(n, times):
    def binary(start, end):
        mid = (end + start) // 2  # 예상 시간

        # 입국심사 가능한 사람 수 (예상 시간을 심사 시간으로 나눈 몫의 합)
        result = sum([mid // t for t in times])

        if n <= result <= n + same_time:
            # 예상 시간(mid) 안에 입국 심사 가능한 사람 수 확인
            # 심사관의 심사 시간이 같을 경우를 고려해서 심사관 수 만큼 여유 줌
            return mid, result
        elif result > n:
            return binary(start, mid - 1)
        else:
            return binary(mid + 1, end)

    t_min = min(times)
    same_time = len(times) - len(set(times))  # 심사시간이 같은 심사관의 수만큼 오차범위 설정
    time, people = binary(t_min, t_min * n)

    if people > n:
        # 예상 심사인원 보다 클 때 최소값 찾기
        tmp = 0
        while True:
            time = max([(time // t) * t for t in times])
            a = sum([time // t for t in times])
            if a == n:
                break
            elif a < n:
                time = tmp
                break
            else:
                tmp = time
                time -= 1
    else:
        time = max((time // t) * t for t in times)

    return time


if __name__ == '__main__':
    print(solution(6, [7, 10]))  # 28
    print(solution(3, [1, 99, 99]))  # 3
    print(solution(7, [10, 10]))  # 40
    print(solution(7, [10, 10, 10]))  # 30
    print(solution(8, [10, 10, 15, 15, 15, 20]))  # 20
    print(solution(6, [1006, 1006, 1025, 1869]))  # 2012
