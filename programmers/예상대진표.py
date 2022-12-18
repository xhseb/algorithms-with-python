def solution(n,a,b):
    answer = 0
    while n != 1:
        answer += 1
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        if a == b:
            break
        a, b = a // 2, b // 2
        n //= 2
    return answer
