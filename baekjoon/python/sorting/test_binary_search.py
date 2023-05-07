from collections import deque


def test_number_1920():
    # N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

    # 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
    # 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

    # M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

    example_list = deque(['5', '4 1 5 2 3', '5', '1 3 7 9 5'])

    def binary_search(array, target, start, end):
        if start > end:
            return None
        mid = int((start + end) / 2)

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, target, start, mid - 1)
        else:
            return binary_search(array, target, mid + 1, end)

    # 이분 탐색 이용
    a_len = int(example_list.popleft())
    a = sorted(list(map(int, example_list.popleft().split(' '))))
    m_len = int(example_list.popleft())
    m = list(map(int, example_list.popleft().split(' ')))
    for i in m:
        if binary_search(a, i, 0, a_len - 1) is not None:
            print(1)
        else:
            print(0)
