def solution(prices):
    answer = [0] * len(prices)
    good_price = 0  # 가격이 떨어지지 않은 가장 큰 수

    for i, p in enumerate(prices):
        decline_count = 0  # 가격이 떨어진 시점을 찾기 위한 변수
        while good_price:
            if good_price > p:
                decline_count += 1  # 가격이 떨어진 시점 카운트
                good_price = prices[i - decline_count - 1]  # 가격이 떨어지기 전 가격

                # 이미 변경된 시간이 있는 지 확인 후 시간 변경
                if answer[i - decline_count] == len(prices) - i - 1 + decline_count:
                    answer[i - decline_count] = decline_count
            else:
                break

        answer[i] = len(prices) - (i + 1)  # 가격이 떨어지지 않을 때 마지막까지 남은 시간
        good_price = p
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
    print(solution([1, 3, 4, 5, 2, 3, 7, 1]))  # [7, 3, 2, 1, 3, 2, 1, 0]
