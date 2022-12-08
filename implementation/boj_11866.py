n, k = map(int, input().split())

list = [1] * n
result = []
c = -1
for i in range(n):
  r = k
  check = 0
  while check != k:
    c += 1
    r -= 1
    if k == 0:
      break
    if c >= n:
      c -= n
    if (list[c] == 1):
      check += 1
  list[c] = 0
  result.append(c + 1)

print('<', end='')
for i in range(len(result)):
  if i != len(result) - 1:
    print(result[i], end=', ')
  else:
    print(result[i], end='')
print('>')