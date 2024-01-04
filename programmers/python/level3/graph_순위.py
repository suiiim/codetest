def solution(n, results):
    answer = 0
    graph = [[0] * (n) for _ in range(n)]

    for a, b in results:
        # 그래프에 이긴 선수의 값 표시
        graph[a - 1][b - 1] = a
        graph[b - 1][a - 1] = a

    for y in range(n):
        for x in range(n):
            if not graph[y][x]:
                continue

            if graph[y][x] == x + 1:
                winner = x + 1
                loser = y + 1
            else:
                winner = y + 1
                loser = x + 1

            for i in range(n):
                if i in (x, y):
                    continue

                # x, y 와의 순위 비교
                if graph[i][winner - 1] == i + 1:
                    # i + 1 > winner > loser
                    graph[loser - 1][i] = i + 1
                    graph[i][loser - 1] = i + 1

                if graph[i][loser - 1] == loser:
                    # winner > loser > i + 1
                    graph[winner - 1][i] = winner
                    graph[i][winner - 1] = winner

    for g in graph:
        if len(list(filter(lambda x: x, g))) == n - 1:
            answer += 1

    return answer


from collections import defaultdict


def solution1(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer


if __name__ == '__main__':
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 2
    print(solution1(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 2
