n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]
#NOTE - 문자열이 iterable하기 때문에 map함수를 사용하여 각 문자를 int형으로 바꿀 수 있다.

result = 0

def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            a[x][y] = 1 - a[x][y]

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            result += 1
        if a == b:
            break
    if a == b:
        break

if a != b:
    result = -1

print(result)