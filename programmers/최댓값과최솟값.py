def solution(s):
    arr = list(map(int, s.split()))
    arr.sort()
    print(arr)
    answer = ''
    answer = str(arr[0]) + ' ' + str(arr[-1])
    return answer