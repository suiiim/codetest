def solution(record: list):
    answer = []
    name = dict()
    for i in record:
        if i.upper().startswith('E'):
            _, user_id, nickname = i.split(' ')
            name[user_id] = nickname
            answer.append([user_id, '님이 들어왔습니다.'])
        elif i.upper().startswith('C'):
            _, user_id, nickname = i.split(' ')
            name[user_id] = nickname
        elif i.upper().startswith('L'):
            _, user_id = i.split(' ')
            answer.append([user_id, '님이 나갔습니다.'])

    return [''.join([name[a[0]], a[1]]) for a in answer]


if __name__ == '__main__':
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
