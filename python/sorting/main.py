def number_2751():
    # N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

    # 첫째 줄에 수의 개수 N(1 <= N <= 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.
    # 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

    # 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

    number_list = []
    for i in range(int(input())):
        number_list.append(int(input()))

    for i in sorted(number_list):
        print(i)


def number_1181():
    # 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오
    # 1. 길이가 짧은 것부터 2. 길이가 같으면 사전 순으로

    # 첫째 줄에 단어의 개수 N이 주어진다. (1 <= N <= 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
    # 주어지는 문자열의 길이는 50을 넘지 않는다.

    # 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러번 입력된 경우에는 한 번씩만 출력한다.

    def sort_logic(x):
        return len(x), x

    word_set = set()
    for i in range(int(input())):
        word_set.add(input())

    for i in sorted(list(word_set), key=lambda x: sort_logic(x)):
        print(i)


if __name__ == '__main__':
    number_2751()
    number_1181()
