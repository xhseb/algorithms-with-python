### 실패 ###
n, m = map(int, input().split())

a = []
b = []


def input_func(a):
    for i in range(n):
        str = input()
        for l in range(m):
            a.append(int(str[l]))


input_func(a)
input_func(b)

result = 0

for i in range(n - 2):
    for l in range(m - 2):
        tmp1 = a
        tmp2 = b
        num = m * i + l
        if tmp1[num:num + 3] != tmp2[num:num + 3]:
            for j in range(3):
                for k in range(3):
                    if (a[num + k + m * j] == 0):
                        a[num + k + m * j] = 1
                    else:
                        a[num + k + m * j] = 0
            result += 1

if (a != b):
    result = -1

print(result)
