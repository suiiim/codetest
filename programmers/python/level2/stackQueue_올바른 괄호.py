def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(1)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return not bool(stack)


if __name__ == '__main__':
    solution("()()")  # true
    solution("(())()")  # true
    solution(")()(")  # false
    solution("(()(")  # false
