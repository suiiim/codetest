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


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))  # 1
    print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
