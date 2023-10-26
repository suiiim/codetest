def solution(genres: list, plays: list):
    answer = []
    album = dict()
    album_count = dict()
    idx = 0
    for k, v in zip(genres, plays):
        album.setdefault(k, list())
        album_count.setdefault(k, int())
        album[k].append((idx, v))
        album_count[k] += int(v)
        idx += 1
    for g in sorted(album_count, key=lambda x: album_count[x], reverse=True):
        idx = 0
        for p in sorted(album[g], key=lambda x: x[1], reverse=True):
            answer.append(p[0])
            idx += 1
            if idx == 2:
                break
    return answer


def solution2(genres, plays):
    from collections import defaultdict
    answer = []
    d_default = defaultdict(list)
    d = dict()
    for i in range(len(genres)):
        d[i] = {genres[i]: plays[i]}
        d_default[genres[i]].append(plays[i])

    d = sorted(d.items(), key=lambda x: [v for k, v in x[1].items()], reverse=True)
    for k, v in d_default.items():
        temp = 0
        for i in v:
            temp += i
        d_default[k] = temp

    d_default = sorted(d_default.items(), key=lambda x: x[1], reverse=True)

    for g, i in d_default:
        temp = []
        for k, v in d:
            if g in v:
                temp.append(k)
        answer.extend(temp[:2])

    return answer


if __name__ == '__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
