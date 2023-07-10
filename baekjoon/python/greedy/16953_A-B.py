from collections import deque

"""
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다. 2를 곱한다. 1을 수의 가장 오른쪽에 추가한다. A를 B로 바꾸는데 필요한 
연산의 최솟값을 구해보자.

첫째 줄에 A, B (1 ≤ A < B ≤ 10**9)가 주어진다.

A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
"""


def solution(example_list):
    a, b = map(int, example_list.popleft().split())

    cnt = 1
    a_set = {a}
    while True:
        if a_set:
            if b in a_set:
                print(cnt)
                break
        else:
            print(-1)
            break
        tmp_set = set()
        for num in a_set:
            if num * 2 <= b:
                tmp_set.add(num * 2)
            if int(f"{num}1") <= b:
                tmp_set.add(int(f"{num}1"))
        cnt += 1
        a_set = tmp_set


if __name__ == '__main__':
    solution(deque(['2 162']))  # 5
    solution(deque(['4 42']))  # -1
    solution(deque(['100 40021']))  # 5
