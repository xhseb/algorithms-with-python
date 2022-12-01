n = int(input())
lens = list(map(int, input().split()))
cost = list(map(int, input().split()))

min = cost[0]
result = 0
for i in range(n - 1):
  min = cost[i] if cost[i] < min else min
  result += min * lens[i]

print(result)