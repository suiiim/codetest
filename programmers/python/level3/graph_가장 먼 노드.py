def solution(n, edge):
    graph = dict()
    result = dict((i, 50000) for i in range(1, n + 1))
    result[1] = 0
    for a, b in edge:
        # 하나의 노드에서 건너갈 수 있는 노드 위치 저장
        graph.setdefault(a, list()).append(b)
        graph.setdefault(b, list()).append(a)

    next_node = list(zip(graph[1], [1] * len(graph[1])))  # 1번 노드에서 갈 수 있는 위치와 다음 노드까지 가는데 이동거리
    while next_node:
        node, cnt = next_node.pop(0)
        if cnt < result[node]:
            result[node] = cnt
            next_node.extend(list(zip(graph[node], [cnt + 1] * len(graph[node]))))

    farthest = max(result.values())
    answer = len(list(filter(lambda x: x == farthest, result.values())))
    return answer


def solution1(n, edge):
    graph = [[] for _ in range(n + 1)]
    distances = [0 for _ in range(n)]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer


if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3
