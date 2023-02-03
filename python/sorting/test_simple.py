from collections import deque


def test_number_2751():
    # N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

    # 첫째 줄에 수의 개수 N(1 <= N <= 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.
    # 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

    # 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

    example_list = deque(['5', '5', '4', '3', '2', '1'])

    number_list = []
    for i in range(int(example_list.popleft())):
        number_list.append(int(example_list.popleft()))

    for i in sorted(number_list):
        print(i)


def test_number_1181():
    # 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오
    # 1. 길이가 짧은 것부터 2. 길이가 같으면 사전 순으로

    # 첫째 줄에 단어의 개수 N이 주어진다. (1 <= N <= 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
    # 주어지는 문자열의 길이는 50을 넘지 않는다.

    # 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러번 입력된 경우에는 한 번씩만 출력한다.

    example_list = deque(['13', 'but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours'])

    def sort_logic(x):
        return len(x), x

    word_set = set()
    for i in range(int(example_list.popleft())):
        word_set.add(example_list.popleft())

    for i in sorted(list(word_set), key=lambda x: sort_logic(x)):
        print(i)


def test_number_1931():
    # 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
    # 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
    # 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
    # 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

    # 첫재 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
    # 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
    # 시작 시간과 끝나는 시간은 2^(31-1)보다 작거나 같은 자연수 또는 0이다.

    # 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
    example_list = deque(['11', '1 4', '3 5', '0 6', '5 7', '3 8', '5 9', '6 10', '8 11', '8 12', '2 13', '12 14'])

    meeting_time = []
    for i in range(int(example_list.popleft())):
        meeting_time.append(tuple(map(int, example_list.popleft().split(' '))))

    temp = 0
    result = 0
    for i, j in sorted(meeting_time, key=lambda x: (x[1], x[0])):
        if int(i) >= temp:
            temp = j
            result += 1
    print(result)
