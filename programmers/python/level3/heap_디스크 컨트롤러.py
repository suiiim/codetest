import heapq


def solution(jobs):
    rs = 0
    next_time = 0
    tmp = []
    for req_time, work in sorted(jobs, key=lambda x: (x[0], x[1])):
        if next_time == req_time:
            heapq.heappush(tmp, work)
            t = heapq.heappop(tmp)
            rs += t + t * len(tmp)
            next_time += t
        elif next_time < req_time:
            if tmp:
                while tmp:
                    t = heapq.heappop(tmp)
                    rs += t + t * len(tmp)
                    next_time += t
                    if next_time < req_time:
                        continue
                    elif next_time == req_time:
                        heapq.heappush(tmp, work)
                        t = heapq.heappop(tmp)
                        rs += t + t * len(tmp)
                        next_time += t
                        break
                    else:
                        heapq.heappush(tmp, work)
                        rs += next_time - req_time
                        break
            else:
                rs += work
                next_time = req_time + work
        else:
            heapq.heappush(tmp, work)
            rs += next_time - req_time

    while tmp:
        t = heapq.heappop(tmp)
        rs += t + t * len(tmp)

    return int((rs) / len(jobs))


if __name__ == '__main__':
    solution([[0, 3], [1, 9], [2, 6]])  # 9
    solution([[0, 4], [0, 3], [0, 2], [0, 1]])  # 5
