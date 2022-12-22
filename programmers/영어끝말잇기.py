def solution(n, words):
    answer = []
    t = words[0][0]
    arr = []
    for i, w in enumerate(words):
        if t != w[0] or arr.count(w) == 1:
            return [i % n + 1, i // n + 1]
        t = w[-1]
        arr.append(w)
    return [0, 0]