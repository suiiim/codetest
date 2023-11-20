def solution(n, wires):
    if n == 2:
        return 0

    def dfs(a):
        visit[a] = 1
        for idx, v in enumerate(point[a]):
            if not visit[idx] and v:
                visit[idx] = 1
                dfs(idx)

    answer = n + 1
    for i in range(len(wires)):
        point = [[0] * n for _ in range(n)]
        visit = [0] * n
        for idx, v in enumerate(wires):
            if idx == i:
                # 전력망 하나씩 제거
                continue
            else:
                point[v[0] - 1][v[1] - 1] = 1
                point[v[1] - 1][v[0] - 1] = 1

        one = 0
        another = 0
        for x in range(n):
            if not visit[x] and sum(point[x]):
                dfs(x)
                if not one:
                    one = sum(visit)  # 하나의 전력망이 이어진 개수를 방문수로 확인
                else:
                    another = sum(visit) - one  # 전체 방문에서 이전 방문수를 빼서 남은 전력망이 이어진 개수 확인
        if not another:  # 하나로만 이어진 전력망을 위한 분기
            another = n - one
        answer = min(abs(one - another), answer)
    return answer


def solution1(n, wires):
    ans = n
    for sub in (wires[i + 1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        # [s.update(v) for _ in sub for v in sub if set(v) & s]
        for _ in sub:  # 모든 값에 따라 한번씩 다 확인
            for v in sub:
                # 첫번째 전력망(sub[0])을 기준으로 다음 전력망 중 현재 전력망의 번호가 있으면 s set에 추가
                if set(v) & s:
                    s.update(v)
        ans = min(ans, abs(2 * len(s) - n))
    return ans


uf = []


def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]


def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa


def solution2(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n + 1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0] - v[1]))

    return answer


if __name__ == '__main__':
    # print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))  # 3
    # print(solution(4, [[1, 2], [2, 3], [3, 4]]))  # 0
    # print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))  # 1
    # print(solution(2, [[1, 2]]))  # 0
    # print(solution(3, [[1, 2], [1, 3]]))  # 1

    print(solution1(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))  # 3
    print(solution1(4, [[1, 2], [2, 3], [3, 4]]))  # 0
    print(solution1(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))  # 1
    print(solution1(2, [[1, 2], [2, 3]]))  # 0
    print(solution1(3, [[1, 2], [1, 3]]))  # 1
