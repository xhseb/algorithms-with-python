n, k = map(int, input().split())

result = 0
while (1):
    if (n == 1):
        break
    if (n % k == 0):
        result += 1
        n /= k
    else:
        result += n % k
        n -= n % k

print(result)
