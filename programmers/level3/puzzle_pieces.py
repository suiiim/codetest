from collections import Counter


def solution(game_board: list, table: list):
    answer = 0

    def block_explore(board, blank, fill):
        total_block = []
        block = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == blank:
                    block.append((row, col))
                if block and (board[row][col] == fill or col == len(board) - 1):
                    for b in total_block:
                        for i in map(lambda x: x[1], block):
                            if (row - 1, i) in b:
                                b.extend(block)
                                block = []
                    if block:
                        total_block.append(block)
                        block = []
        return total_block

    def compare_block(a, b):
        for _ in range(4):
            a = list(map(lambda x: (x[0] - min([i[0] for i in a]), x[1] - min([i[1] for i in a])), a))
            b = list(map(lambda x: (x[0] - min([i[0] for i in b]), x[1] - min([i[1] for i in b])), b))
            if sorted(a) == sorted(b):
                return True
            else:
                row = max(max([i[0] for i in a]), max([i[1] for i in a]))
                a = list(map(lambda x: (x[1], x[0] + (row - x[0] * 2)), a))
        return False

    game_block = block_explore(game_board, 0, 1)
    table_block = block_explore(table, 1, 0)

    for t in table_block:
        for g in filter(lambda x: len(x) == len(t), game_block):
            if compare_block(t, g):
                answer += len(g)
                game_block.remove(g)
                break

    return answer


if __name__ == '__main__':
    print(solution(
        [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
        [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]
    ))
    print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
