from collections import deque

"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오. 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
"""


# DP로 LIS의 길이 구하기
# dp[i] = i번째 원소로 끝나는 가장 긴 증가하는 부분 수열의 길이
# dp[i] = 0~i-1번째 인덱스에 있고 i번째 수보다 작은 수들에 대해 가장 긴 증가하는 부분수열 길이의 최댓값+1
def solution(example_list):
    cnt = int(example_list.popleft())
    a = list(map(int, example_list.popleft().split()))
    dp = [0] * cnt

    dp[0] = 1
    for i in range(1, cnt):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[j] + 1, dp[i])
            dp[i] = max(dp[i], 1)
    print(max(dp))


if __name__ == '__main__':
    solution(deque(['6', '10 20 10 30 20 50']))  # 4
