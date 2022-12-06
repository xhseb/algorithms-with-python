num = int(input())
data = []
for i in range(num):
  tmp = int(input())
  if (tmp != 0):
    data.append(tmp)
  else:
    data.pop()

print(sum(data))