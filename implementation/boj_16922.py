from itertools import combinations_with_replacement
from collections import Counter
num = int(input())
data = [1, 5, 10, 50]
li = list(combinations_with_replacement(data, num))
a = []
for i in li:
  a.append(sum(i))

result = Counter(a)
print(len(result))