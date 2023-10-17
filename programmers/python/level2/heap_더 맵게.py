from heapq import heappush, heappop, heapify


def solution(scoville, K):
    answer = 0

    heapify(scoville)
    while True:
        if scoville[0] >= K:
            break
        if len(scoville) >= 2:
            x = heappop(scoville)
            y = heappop(scoville)
            heappush(scoville, x + y * 2)
            answer += 1
        else:
            answer = -1
            break

    return answer


if __name__ == '__main__':
    solution([1, 2, 3, 9, 10, 12], 7)  # 2
