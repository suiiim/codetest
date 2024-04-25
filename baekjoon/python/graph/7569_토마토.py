"""
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩
넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다. 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지
않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의
영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보
관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다. 토마토를 창고에 보관하는 격자모양의 상자들의
크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구
하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수,
N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자
부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정
보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은
익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.
토마토가 하나 이상 있는 경우만 입력으로 주어진다.

여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는
상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
# -1

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
# 4

4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
# 0
"""
import sys

input = sys.stdin.readline


# Memory 87556 KB
# Time 1620 ms
def solution():
    n, m, h = map(int, input().split())
    direction = [(0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
    box = [[input().split() for _ in range(m)] for _ in range(h)]
    start = []
    result = 0

    for z in range(h):
        for x in range(m):
            for y in range(n):
                if box[z][x][y] == '1':
                    start.append([z, x, y])

    while start:
        tmp = []
        while start:
            z, x, y = start.pop()
            for z_, x_, y_ in direction:
                if 0 <= x + x_ < m and 0 <= y + y_ < n and 0 <= z + z_ < h and box[z + z_][x + x_][y + y_] == '0':
                    box[z + z_][x + x_][y + y_] = '1'
                    tmp.append([z + z_, x + x_, y + y_])
        result += 1
        start = tmp

    if sum([sum([list(filter(lambda x: x == '0', i)) for i in b], []) for b in box], []):
        print(-1)
    else:
        print(result - 1)


solution()

# Memory 48496 KB
# Time 744 ms
from collections import deque


def main():
    width, depth, height = map(int, input().split())
    box = list()

    process = deque()

    for i in range(height):
        plate = list()
        for j in range(depth):
            row = list(map(int, input().split()))
            plate.append(row)
            for k, state in enumerate(row):
                if state == 1:
                    process.append((i, j, k))
        box.append(plate)

    if not process:
        print('-1')
        return

    days = 0
    next_process = deque()
    while process or next_process:
        if not process:
            process, next_process = next_process, deque()
            days += 1
        if not process:
            days -= 1
            break

        x, y, z = process.popleft()

        if x > 0 and box[x - 1][y][z] == 0:
            box[x - 1][y][z] = 1
            next_process.append((x - 1, y, z))
        if x < height - 1 and box[x + 1][y][z] == 0:
            box[x + 1][y][z] = 1
            next_process.append((x + 1, y, z))
        if y > 0 and box[x][y - 1][z] == 0:
            box[x][y - 1][z] = 1
            next_process.append((x, y - 1, z))
        if y < depth - 1 and box[x][y + 1][z] == 0:
            box[x][y + 1][z] = 1
            next_process.append((x, y + 1, z))
        if z > 0 and box[x][y][z - 1] == 0:
            box[x][y][z - 1] = 1
            next_process.append((x, y, z - 1))
        if z < width - 1 and box[x][y][z + 1] == 0:
            box[x][y][z + 1] = 1
            next_process.append((x, y, z + 1))

    not_rippen = False
    for plate in box:
        for row in plate:
            if 0 in row:
                not_rippen = True
                break
        if not_rippen:
            break

    if not_rippen:
        print('-1')
    else:
        print(days)


main()
