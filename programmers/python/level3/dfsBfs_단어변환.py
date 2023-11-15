from collections import deque


def solution(begin, target, words):
    if target in words:
        answer = 1
        dq = deque([begin])
        access = []
        while dq:
            tmp = dq.popleft()
            print(tmp)
            for idx in range(len(tmp)):
                # words 리스트 중 한 번에 한개의 알파벳만 바꿀 수 있는 단어 리스트 추출
                a = list(filter(lambda x: x.startswith(tmp[:idx]) and x.endswith(tmp[idx + 1:]) and x != tmp and x not in access, words))
                print(a)
                access.extend(a)
            if dq:
                continue  # 아직 확인할 단어가 남으면 계속
            else:
                if access:
                    if target in access:
                        break  # 변환된 단어 중 타겟이 있을 때
                    else:
                        dq = deque(access)
                        access = []
                        answer += 1  # 다음 변환된 단어 확인
                else:
                    answer = 0  # 변환 가능한 단어가 없을 때
                    break
        return answer
    else:
        return 0


if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
