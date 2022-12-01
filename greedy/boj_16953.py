a, b = map(int, input().split())

result = 1
while (True):
    if b == a:
        break
    elif b < a:
        result = -1
        break
    elif b % 10 == 1:
        b //= 10
        result += 1
    elif b % 2 == 0:
        b //= 2
        result += 1
    else:
        result = -1
        break

print(result)