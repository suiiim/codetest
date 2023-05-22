from collections import deque


def test_number_12761():
    # 동규와 주미는 일직선 상의 돌 다리 위에있다. 돌의 번호는 0 부터 100,000 까지 존재하고 동규는 N번 돌 위에, 주미는 M번 돌 위에 위치하고 있다. 동규는 주미가 너무 보고싶기
    # 때문에 최대한 빨리 주미에게 가기 위해 A, B 만큼의 힘을 가진 스카이 콩콩을 가져왔다. 동규가 정한 다리를 건너는 규칙은 턴 방식인데, 한 턴에 이동할 수 있는 거리는 이러하다.
    # 현 위치에서 +1칸, -1칸을 이동할 수 있고, 스카이 콩콩을 이용해 현 위치에서 A나 B만큼 좌우로 점프할 수 있으며, 순간적으로 힘을 모아 현 위치의 A배나 B배의 위치로 이동을
    # 할 수 있다. 예를 들어 지금 동규가 7번 돌 위에 있고 스카이 콩콩의 힘이 8이면 그냥 점프를 해서 15번 돌에 갈 수도 있고, 순간적으로 힘을 모아 56번 돌에 갈 수도 있다는 것이다.
    # 주어진 8가지의 방법 중 적절한 방법을 골라서 최대한 빨리 동규가 주미를 만날 수 있게 도와주자. 단, 이동 과정에서 100,000보다 크거나 0보다 작은 번호의 돌은 존재하지 않으므로
    # 갈 수 없고, 같은 방법을 계속 사용해도 되며 항상 도달할 수 있는 케이스만 주어진다.

    # 입력의 첫 줄에 스카이 콩콩의 힘 A와 B, 그리고 동규의 현재위치 N, 주미의 현재 위치 M이 주어진다. (단, 2 <= A, B <= 30 이고 0 <= N, M <= 100,000)

    # 동규가 주미에게 도달하기 위한 최소한의 이동 횟수를 출력하라.

    example_list = deque(['2 3 1 20'])
    # example_list = deque(['3 7 2 98500'])

    a, b, n, m = list(map(int, example_list.popleft().split()))
    answer = 0
    result = {n}
    while m not in result:
        tmp = set()
        for r in result:
            if r + 1 <= 100000:
                tmp.add(r + 1)
            if r - 1 >= 0:
                tmp.add(r - 1)
            for num in [a, b]:
                if r + num <= 100000:
                    tmp.add(r + num)
                if r * num <= 100000:
                    tmp.add(r * num)
                if r - num >= 0:
                    tmp.add(r - num)
        answer += 1
        result = tmp

    print(answer)


def test_number_1926():
    # 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고
    # 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

    # 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의
    # 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

    # 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

    example_list = deque(['6 5', '1 1 0 1 1', '0 1 1 0 0', '0 0 0 0 0', '1 0 1 1 1', '0 0 1 1 1', '0 0 1 1 1'])

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
