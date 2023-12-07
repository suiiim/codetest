from collections import defaultdict


def solution(tickets):
    answer = ["ICN"]
    city_hash = {}

    for a, b in tickets:
        city_hash.setdefault(a, [])
        city_hash[a].append(b)

    def travel(city_ticket, order):
        next_city = city_ticket[order[-1]] if order[-1] in city_ticket else []
        next_city.sort()  # 알파벳 순으로 정렬
        if next_city:
            # 다음 종착지가 있으면 알파벳 순으로 여행
            for i in range(len(next_city)):
                city_ticket[order[-1]] = [*next_city[:i], *next_city[i + 1:]]
                rs = travel(city_ticket, [*order, next_city[i]])
                if rs:
                    # 여행을 끝마치면 결과값 반환
                    return rs
                else:
                    city_ticket[order[-1]] = next_city
        else:
            # 다음 종착지가 없을 경우 남은 ticket 이 있는지 확인
            if sum(city_ticket.values(), []):
                return []
            else:
                return order

    answer = travel(city_hash, answer)
    return answer


def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution1(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer


if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))  # ["ICN", "JFK", "HND", "IAD"]
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    print(solution([["ICN", "A"], ["A", "B"], ["ICN", "C"], ["C", "ICN"]]))  # ["ICN", "C", "ICN", "A", "B"]
    print(solution([["ICN", "A"], ["ICN", "A"], ["A", "ICN"], ["A", "C"]]))  # ["ICN", "A", "ICN", "A", "C"]
