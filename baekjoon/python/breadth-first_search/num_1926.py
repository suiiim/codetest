from collections import deque

"""
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고
정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의
정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
"""


def solution(example_list):
    row, col = list(map(int, example_list.popleft().split()))
    paint = [[0 for _ in range(col + 2)]]
    for r in range(row):
        tmp = [0]
        tmp.extend(list(map(int, example_list.popleft().split())))
        tmp.append(0)
        paint.append(tmp)
    paint.append([0 for _ in range(col + 2)])

    total = sum(map(lambda i: sum(i), paint))
    cnt = 0
    wide = 0
    while total:
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                if paint[r][c]:
                    cnt += 1
                    tmp_wide = 1
                    paint[r][c] = 0
                    tmp = [(r, c)]
                    while tmp:
                        x, y = tmp.pop()
                        for a, b in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            if paint[x + a][y + b]:
                                paint[x + a][y + b] = 0
                                tmp_wide += 1
                                tmp.append((x + a, y + b))
                    total -= tmp_wide
                    wide = max(wide, tmp_wide)

    print(cnt)
    print(wide)


if __name__ == '__main__':
    solution(deque(['6 5', '1 1 0 1 1', '0 1 1 0 0', '0 0 0 0 0', '1 0 1 1 1', '0 0 1 1 1', '0 0 1 1 1']))
