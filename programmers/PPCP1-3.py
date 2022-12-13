def solution(queries):
    answer = []
    for i in queries:
        if i[0] == 1 and i[1] == 1:
            answer.append('Rr')
        elif i[1] <= 4 ** (i[0] - 2):
            answer.append('RR')
        elif 4 ** (i[0] - 2) < i[1] and i[1] <= 4 ** (i[0] - 1) - 4 ** (i[0] - 2):
            if i[1] % 4 == 1:
                answer.append('RR')
            elif i[1] % 4 == 2 or i[1] % 4 == 3:
                answer.append('Rr')
            else:
                answer.append('rr')
        else:
            answer.append('rr')
    return answer