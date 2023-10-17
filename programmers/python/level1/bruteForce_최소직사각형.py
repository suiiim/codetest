def solution(sizes):
    x, y = 0, 0
    for w, h in sizes:
        if w > h:
            x = max(x, w)
            y = max(y, h)
        else:
            x = max(x, h)
            y = max(y, w)
    return x * y


if __name__ == '__main__':
    solution([[60, 50], [30, 70], [60, 30], [80, 40]])  # 4000
    solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])  # 120
    solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])  # 133
