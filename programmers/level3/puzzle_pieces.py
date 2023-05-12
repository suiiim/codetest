from collections import deque


def solution(game_board: list, table: list):
    answer = -1

    # table 블록추출 (dfs, bfs사용)
    def block_explore(board, blank, fill):
        total_block = []
        block = []
        for row in range(6):
            for col in range(6):
                if board[row][col] == blank:
                    block.append((row, col))
                if block and (board[row][col] == fill or col == 5):
                    for b in total_block:
                        for i in map(lambda x: x[1], block):
                            if (row - 1, i) in b:
                                b.extend(block)
                                block = []
                    if block:
                        total_block.append(block)
                        block = []
        return total_block

    game_block = block_explore(game_board, 0, 1)
    table_block = block_explore(table, 1, 0)

    def minimum_value(ll):
        ll = list(map(lambda x: (x[0] - min([i[0] for i in ll]), x[1] - min([i[1] for i in ll])), ll))
        return ll

    for t in table_block:
        for g in filter(lambda x: len(x) == len(t), game_block):
            t = list(map(lambda x: (x[0] - min([i[0] for i in t]), x[1] - min([i[1] for i in t])), t))
            g = list(map(lambda x: (x[0] - min([i[0] for i in g]), x[1] - min([i[1] for i in g])), g))
            print()

    print()

    # game_board 빈곳 추출

    # 탐색 함수 구현
    def dfs():
        pass

    # 턴함수 구현
    def block_turn():
        pass

    return answer


if __name__ == '__main__':
    print(solution(
        [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
        [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]
    ))
    print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
