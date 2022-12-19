def solution(lottos, win_nums):
    answer = []
    arr = [i for i in lottos if i in win_nums]
    if len(arr) != 0:
        answer.append(7 - len(arr))
    else:
        answer.append(6)
    if lottos.count(0) != 6:
        answer.insert(0, answer[0] - lottos.count(0))
    else:
        answer.insert(0, 1)
    return answer