from collections import deque

"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 
번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 
<그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
        0 1 1 0 1 0 0           0 1 1 0 2 0 0
        0 1 1 0 1 0 1           0 1 1 0 2 0 2
        1 1 1 0 1 0 1           1 1 1 0 2 0 2
        0 0 0 0 1 1 1           0 0 0 0 2 2 2
        0 1 0 0 0 0 0           0 3 0 0 0 0 0
        0 1 1 1 1 1 0           0 3 3 3 3 3 0
        0 1 1 1 0 0 0           0 3 3 3 0 0 0
          < 그림 1 >               < 그림 2 >    

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
"""


def solution(example_list):
    result = []

    size = int(example_list.popleft())
    map_img = [[0] * (size + 2)] * (size + 2)
    for i in range(1, size + 1):
        graph = [int(x) for x in ''.join(["0", example_list.popleft(), "0"])]
        map_img[i] = graph

    a, b = 1, 1
    while True:
        if map_img[a][b]:
            tmp = [(a, b)]
            map_img[a][b] = 0
            cnt = 1
            while tmp:
                x, y = tmp.pop()
                for _x, _y in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                    if map_img[_x][_y]:
                        tmp.append((_x, _y))
                        map_img[_x][_y] = 0
                        cnt += 1
            result.append(cnt)
        else:
            if b < size:
                b += 1
            else:
                if a == size:
                    break
                else:
                    b = 1
                    a += 1

    print(len(result))
    for i in sorted(result):
        print(i)


def solution1(example_list):
    result = []

    def dfs(x, y):
        cnt = 0
        if map_img[x][y]:
            map_img[x][y] = 0
            cnt += 1
            for x_, y_ in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if map_img[x_][y_]:
                    cnt += dfs(x_, y_)
        return cnt

    size = int(example_list.popleft())
    map_img = [[0] * (size + 2)] * (size + 2)
    for i in range(1, size + 1):
        graph = [int(x) for x in ''.join(["0", example_list.popleft(), "0"])]
        map_img[i] = graph

    for a in range(1, size + 1):
        for b in range(1, size + 1):
            tmp = dfs(a, b)
            if tmp:
                result.append(tmp)

    print(len(result))
    for i in sorted(result):
        print(i)


if __name__ == '__main__':
    # solution(deque(['7', '0110100', '0110101', '1110101', '0000111', '0100000', '0111110', '0111000']))  # 3 7 8 9
    solution1(deque(['7', '0110100', '0110101', '1110101', '0000111', '0100000', '0111110', '0111000']))  # 3 7 8 9
