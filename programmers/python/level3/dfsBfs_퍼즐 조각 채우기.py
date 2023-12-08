from collections import Counter


def solution(game_board: list, table: list):
    answer = 0
    length = len(table)
    piece_list = []
    piece = []

    def dfs(x, y, board, flag):
        board[x][y] = 0 if flag else 1
        for x_, y_ in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
            if 0 <= x_ < length and 0 <= y_ < length and board[x_][y_] == flag:
                piece.append([x_, y_])
                dfs(x_, y_, board, flag)

    def spin(one):
        max_n = max(sum(one, []))
        other = []
        for x, y in one:
            other.append([y, max_n - x])
        # 찾은 조각은 최솟값으로 맞춰서 반환
        x_min = min([x[0] for x in other])
        y_min = min([x[1] for x in other])
        return sorted(list(map(lambda o: [o[0] - x_min, o[1] - y_min], other)))

    # table 에 있는 조각 찾기
    for b in range(length):
        for a in range(length):
            if table[a][b]:
                piece = [[a, b]]
                dfs(a, b, table, 1)
                # 찾은 조각은 최솟값으로 맞춰서 piece_list 에 저장
                a_min = min([x[0] for x in piece])
                b_min = min([x[1] for x in piece])
                piece_list.append(sorted(list(map(lambda x: [x[0] - a_min, x[1] - b_min], piece))))

    # game_board 에 있는 조각 찾기
    for b in range(length):
        for a in range(length):
            if not game_board[a][b]:
                piece = [[a, b]]
                dfs(a, b, game_board, 0)
                # 찾은 조각은 최솟값으로 맞춰서 piece_list 와 비교
                a_min = min([x[0] for x in piece])
                b_min = min([x[1] for x in piece])
                tmp = sorted(list(map(lambda x: [x[0] - a_min, x[1] - b_min], piece)))
                same_flag = False
                # 빈칸 개수가 다른 조각만 확인
                for p in filter(lambda x: len(x) == len(tmp), piece_list):
                    for _ in range(4):
                        if p == tmp:
                            same_flag = True
                            break
                        else:
                            # 값이 다르면 최대 3번까지 조각 회전
                            tmp = spin(tmp)
                    if same_flag:
                        break
                if same_flag:
                    # 조각 모양이 같으면 piece_list 에서 지운 후 조각의 크기를 answer 에 더함
                    piece_list.remove(tmp)
                    answer += len(tmp)
    return answer


if __name__ == '__main__':
    print(solution(
        [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
        [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]
    ))  # 14
    print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))  # 0
    print(solution([[1, 0, 1], [0, 0, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]]))  # 4
