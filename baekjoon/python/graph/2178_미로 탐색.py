from collections import deque

"""
N×M크기의 배열로 표현되는 미로가 있다.
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 
지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
"""


def solution(example_list):
    def bfs(start):
        stack = []
        cnt[0] += 1
        for x, y in start:
            for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                if maze[x + dx][y + dy]:
                    maze[x + dx][y + dy] = 0
                    stack.append([x + dx, y + dy])
        return stack

    n, m = list(map(int, example_list.popleft().split()))
    maze = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    for n_ in range(1, n + 1):
        for m_, v in enumerate(example_list.popleft()):
            if v == '1':
                maze[n_][m_ + 1] = 1

    cnt = [1]
    result = [[1, 1]]
    while [n, m] not in result:
        result = bfs(result)
    print(cnt[0])


if __name__ == '__main__':
    solution(deque(['4 6', '101111', '101010', '101011', '111011']))
    solution(deque(['4 6', '110110', '110110', '111111', '111101']))
    solution(deque(['2 25', '1011101110111011101110111', '1110111011101110111011101']))
    solution(deque(['7 7', '1011111', '1110001', '1000001', '1000001', '1000001', '1000001', '1111111']))
