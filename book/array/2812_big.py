"""
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 주어진다. 둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다. 입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.

4 2
1924

7 3
1231234

10 4
4177252841
"""

n, k = map(int, input().split())
num = str(input())

result = []
for v in num:
    while k and result and result[-1] < v:
        k -= 1
        result.pop()
    result.append(v)
if k > 0:
    result = result[:-k]
print(''.join(result))
