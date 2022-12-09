check = list(map(int, input()))
set = [0 for i in range(9)]
for c in check:
  if c == 9:
    set[6] += 1
  else:
    set[c] += 1
if set[6]%2 == 0:
  set[6] //= 2
else:
  set[6] //= 2
  set[6] += 1

max = 0
for i in range(9):
  if max < set[i]:
    max = set[i]
print(max)