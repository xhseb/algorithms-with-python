tx, ty = input()
x, y = ord(tx) - ord('a') + 1, int(ty)
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

result = 0
for step in steps:
  next_x = x + step[0]
  next_y = y + step[1]
  if next_x >= 1 and next_x <= 8 and next_y >= 1 and next_y <= 8:
    result += 1
print(result)