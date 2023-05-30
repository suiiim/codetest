from collections import deque
from itertools import permutations

"""
    +---+        
    | D |        
+---+---+---+---+
| E | A | B | F |
+---+---+---+---+
    | C |        
    +---+   
주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다. A, B, C, D, E, F에 쓰여 있는 수가 주어진다. 지민이는 현재 
동일한 주사위를 N^3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N 크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.
N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. 둘째 줄에 주사위에 쓰여 있는 수가 주어진다. 위의 그림에서 A, B, C, D, E, F에 쓰여 있는 수가 차례대로 주어진다. N은 1,000,000보다 작거나 
같은 자연수이고, 쓰여 있는 수는 50보다 작거나 같은 자연수이다.

첫째 줄에 문제의 정답을 출력한다.
"""


def solution(example_list):
    n = int(example_list.popleft())
    num = list(map(int, example_list.popleft().split()))
    left = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}
    if n == 0:
        print(0)
    elif n == 1:
        print(sum(num) - max(num))
    else:
        answer = 0
        num_tmp = sorted([min(num[0], num[5]), min(num[1], num[4]), min(num[2], num[3])])
        if (n - 2):
            answer += (((n - 2) ** 2) * 5 + (n - 2) * 4) * num_tmp[0]
        answer += (4 + (n - 2) * 8) * sum(num_tmp[:2])
        answer += 4 * sum(num_tmp)
        print(answer)


if __name__ == '__main__':
    solution(deque(['5', '1 1 1 1 1 1']))  # 125
    solution(deque(['10', '50 39 25 14 48 7']))  # 4132
    solution(deque(['1000000', '1 2 3 4 5 6']))  # 5000008000000
    solution(deque(['2', '1 2 3 4 5 6']))
    solution(deque(['3', '1 2 3 4 5 6']))
    solution(deque(['1000000', '50 50 50 50 50 50']))
    solution(deque(['10', '1 1 1 1 50 1']))
