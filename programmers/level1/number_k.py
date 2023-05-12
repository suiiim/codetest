def solution1(array: list, commands: list):
    answer = []
    for i, j, k in commands:
        if i:
            i -= 1
        if j == len(array):
            j = None
        answer.append(sorted(array[i:j])[k - 1])
    return answer


def solution2(array: list, commands: list):
    answer = []
    for item in commands:
        i = int(item[0]) - 1
        j = int(item[1])
        k = int(item[2]) - 1
        temp = array[i:j]
        temp.sort()
        answer.append(temp[k])
    return answer


if __name__ == '__main__':
    print(solution1([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
    print(solution2([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
