def solution(input_string):
    arr = [0] * 26
    for i in range(len(input_string) - 1):
        if input_string[i] != input_string[i + 1]:
            arr[ord(input_string[i]) - ord('a')] += 1
    arr[ord(input_string[len(input_string) - 1]) - ord('a')] += 1
    answer = ''
    for i in range(26):
        if arr[i] > 1:
            answer += chr(i + 97)
    if answer == '':
        answer = 'N'
    return answer