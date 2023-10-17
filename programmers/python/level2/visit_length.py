def solution(dirs: str):
    x, y = 0, 0
    cross = set()
    for i in dirs.upper():
        if i == 'U' and y + 1 < 6:
            cross.add(((x, y), (x, y + 1)))
            y += 1
        elif i == 'D' and y - 1 > -6:
            cross.add(((x, y - 1), (x, y)))
            y -= 1
        elif i == 'R' and x + 1 < 6:
            cross.add(((x, y), (x + 1, y)))
            x += 1
        elif i == 'L' and x - 1 > -6:
            cross.add(((x - 1, y), (x, y)))
            x -= 1

    return len(cross)


if __name__ == '__main__':
    print(solution('ULURRDLLU'))
    print(solution('LULLLLLLU'))
