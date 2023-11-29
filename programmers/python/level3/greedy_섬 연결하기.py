def solution(n, costs):
    # kruskal 알고리즘
    answer = 0
    costs.sort(key=lambda x: x[2])  # cost 기준으로 오름차순 정렬
    link = set([costs[0][0]])  # 집합

    while len(link) != n:
        for i, cost in enumerate(costs):
            if cost[0] in link and cost[1] in link:
                continue
            if cost[0] in link or cost[1] in link:
                link.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer


def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)


def solution1(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer


if __name__ == '__main__':
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))  # 4
    print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]))  # 104
    print(solution(8, [[0, 1, 1], [1, 2, 2], [1, 7, 4], [2, 5, 3], [2, 7, 3], [3, 4, 2], [3, 6, 1], [4, 6, 1], [5, 6, 6]]))  # 17

    print(solution1(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))  # 4
    print(solution1(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]))  # 104
    print(solution1(8, [[0, 1, 1], [1, 2, 2], [1, 7, 4], [2, 5, 3], [2, 7, 3], [3, 4, 2], [3, 6, 1], [4, 6, 1], [5, 6, 6]]))  # 17
