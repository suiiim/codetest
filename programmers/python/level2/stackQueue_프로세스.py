import queue


def solution(priorities, location):
    answer = 0
    q = queue.Queue()
    for i, p in zip(range(len(priorities)), priorities):
        q.put((i, p))
    priorities.sort(reverse=True)
    while q:
        tmp = q.get()
        if tmp[1] == priorities[answer]:
            answer += 1
            if tmp[0] == location:
                break
        else:
            q.put(tmp)

    return answer


def solution1(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))  # 1
    print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
