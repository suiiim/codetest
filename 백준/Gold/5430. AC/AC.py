for i in range(int(input())):
    idx = [0, 0]
    flag = True
    dump_len = 0
    for func in input():
        if func == 'R':
            flag = not flag
        elif func == 'D':
            dump_len += 1
            if flag:
                idx[0] += 1
            else:
                idx[1] -= 1

    if int(input()) < dump_len:
        print('error')
        tmp = input()
    else:
        arr = list(input()[1:-1].split(','))
        idx[1] = len(arr) if idx[1] == 0 else idx[1]
        if flag:
            print(f"[{','.join(arr[idx[0]:idx[1]])}]")
        else:
            print(f"[{','.join(reversed(arr[idx[0]:idx[1]]))}]")