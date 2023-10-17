def solution(n, m, x, y, r, c, k):
    def func(f):
        for i in ['d', 'l', 'r', 'u']:
            if f == i:
                return f

    move = ''
    if r - x > 0:
        move += 'd' * (r - x)
    else:
        move += 'u' * (x - r)
    if y - c > 0:
        move += 'l' * (y - c)
    else:
        move += 'r' * (c - y)

    if k < len(move):
        return 'impossible'
    elif (k - len(move)) % 2 != 0:
        return 'impossible'
    elif k == len(move):
        return ''.join(sorted(move, key=func))
    else:
        left = k - len(move)
        if n - r > 0 and r != 1:
            tmp = min(int(n - r if n - r < left / 2 else left / 2), r - n)
            move += 'lr' * tmp
            left -= tmp * 2
            print(tmp, move, left)
        if m - c > 0 and c != 1:
            tmp = min(int(m - c if m - c < left / 2 else left / 2), c - m)
            move += 'ud' * tmp
            left -= tmp * 2
            print(tmp, move, left)
        move = sorted(move, key=func)
        print(left)
        if left:
            move += 'rl' * int(left / 2)

    return ''.join(move)


if __name__ == '__main__':
    print(solution(3, 4, 2, 3, 3, 1, 5))
