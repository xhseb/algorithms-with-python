n = int(input())
board = [[0] * 100 for i in range(100)]

for _ in range(n):
  x, y = map(int, input().split())
  for j in range(10):
    for k in range(10):
      board[x + j][y + k] = 1

result = 0
for m in board:
  result += m.count(1)
print(result)