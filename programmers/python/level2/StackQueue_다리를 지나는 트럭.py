from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    dq = deque()
    for truck in truck_weights:
        time += 1
        # 하중을 견디는 크기가 넘을 때 첫번째 트럭부터 통과
        while weight - truck < 0:
            tr, ti = dq.popleft()
            print('start', weight)
            weight += tr
            print(f"{time} - {ti} =", time - ti)
            # 이미 다리를 통과한 트럭은 패스
            if bridge_length < time - ti:
                continue
            time += bridge_length - (time - ti)
            print(time, list(dq))
            print('end', weight)
        # 다음 트럭 다리 건너기
        dq.append([truck, time])
        weight -= truck
        print(time, list(dq), weight)
    print(time)
    if dq:
        tr, ti = dq[-1]
        print(f"{time} - {ti} =", time - ti)
        time += bridge_length - (time - ti)
    return time


def solution1(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step


if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))  # 8
    print(solution(100, 100, [10]))  # 101
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
    print(solution(8, 5, [3, 3, 3, 3]))  # 33
    print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))  # 19
