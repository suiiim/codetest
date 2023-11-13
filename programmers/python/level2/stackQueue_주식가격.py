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


"""
테스트 1 〉	통과 (230.81ms, 18.8MB)
테스트 2 〉	통과 (151.54ms, 17.5MB)
테스트 3 〉	통과 (252.96ms, 19.5MB)
테스트 4 〉	통과 (195.11ms, 18.2MB)
테스트 5 〉	통과 (157.11ms, 16.9MB)
"""


def solution1(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


"""
테스트 1 〉	통과 (155.59ms, 18.9MB)
테스트 2 〉	통과 (131.82ms, 17.6MB)
테스트 3 〉	통과 (192.73ms, 19.5MB)
테스트 4 〉	통과 (138.11ms, 18.3MB)
테스트 5 〉	통과 (92.29ms, 16.8MB)
"""


def solution2(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer


"""
테스트 1 〉	통과 (34.11ms, 18.8MB)
테스트 2 〉	통과 (25.63ms, 17.6MB)
테스트 3 〉	통과 (38.07ms, 19.5MB)
테스트 4 〉	통과 (29.53ms, 18.2MB)
테스트 5 〉	통과 (20.44ms, 16.8MB)
"""

if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
    print(solution([1, 3, 4, 5, 2, 3, 7, 1]))  # [7, 3, 2, 1, 3, 2, 1, 0]
    print(solution([2, 2, 3, 6, 5, 4, 5, 6, 1]))  # [8, 7, 6, 1, 1, 3, 2, 1, 0]

    print(solution1([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
    print(solution1([1, 3, 4, 5, 2, 3, 7, 1]))  # [7, 3, 2, 1, 3, 2, 1, 0]
    print(solution1([2, 2, 3, 6, 5, 4, 5, 6, 1]))  # [8, 7, 6, 1, 1, 3, 2, 1, 0]

    print(solution2([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
    print(solution2([1, 3, 4, 5, 2, 3, 7, 1]))  # [7, 3, 2, 1, 3, 2, 1, 0]
    print(solution2([2, 2, 3, 6, 5, 4, 5, 6, 1]))  # [8, 7, 6, 1, 1, 3, 2, 1, 0]
