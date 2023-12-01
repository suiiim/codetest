from collections import deque
import time


def solution1(x, y, n):
    answer = 0
    bfs = deque([])
    if y % 2 != 0 and y % 3 != 0 and (y - x) % n != 0:
        return -1
    else:
        bfs.append((x + n, answer + 1))
        bfs.append((x * 2, answer + 1))
        bfs.append((x * 3, answer + 1))

    while x != y:
        if bfs:
            x, answer = bfs.popleft()
        else:
            return -1
        if x + n <= y and not x + n in map(lambda i: i[0], bfs):
            bfs.append((x + n, answer + 1))
        if x * 2 <= y and not x * 2 in map(lambda i: i[0], bfs):
            bfs.append((x * 2, answer + 1))
        if x * 3 <= y and not x * 3 in map(lambda i: i[0], bfs):
            bfs.append((x * 3, answer + 1))
        if y in map(lambda i: i[0], bfs):
            answer = list(filter(lambda i: i[0] == y, bfs))[0][1]
            break

    return answer


def solution2(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)

    while dp:
        if y in dp:
            return answer
        else:
            dp_y = set()
            for i in dp:
                if i + n <= y:
                    dp_y.add(i + n)
                if i * 2 <= y:
                    dp_y.add(i * 2)
                if i * 3 <= y:
                    dp_y.add(i * 3)
            dp = dp_y
            answer += 1

    return -1


def solution3(x: int, y: int, n: int) -> int:
    DP = [int(1e9)] * (y + 1)
    DP[x] = 0

    if x + n <= y:
        DP[x + n] = 1
    if x * 2 <= y:
        DP[x * 2] = 1
    if x * 3 <= y:
        DP[x * 3] = 1

    for i in range(x, y + 1):
        if i >= n:
            DP[i] = min(DP[i], DP[i - n] + 1)
        if i % 2 == 0 and i // 2:
            DP[i] = min(DP[i], DP[i // 2] + 1)
        if i % 3 == 0 and i // 3:
            DP[i] = min(DP[i], DP[i // 3] + 1)
    if DP[y] != int(1e9):
        return DP[y]
    return -1


if __name__ == '__main__':
    start = time.time()
    print(solution1(1, 500, 5))  # -1
    print(solution1(10, 40, 5))  # 2
    print(solution1(10, 40, 30))  # 1
    print(solution1(10, 50, 30))  # 2
    print(solution1(2, 5, 4))  # -1
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution2(1, 500, 5))  # -1
    print(solution2(10, 40, 5))  # 2
    print(solution2(10, 40, 30))  # 1
    print(solution2(10, 50, 30))  # 2
    print(solution2(2, 5, 4))  # -1
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution3(1, 500, 5))  # -1
    print(solution3(10, 40, 5))  # 2
    print(solution3(10, 40, 30))  # 1
    print(solution3(10, 50, 30))  # 2
    print(solution3(2, 5, 4))  # -1
    end = time.time()
    print(end - start)
