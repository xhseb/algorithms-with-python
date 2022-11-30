#### 첫번째 로직 #####
# n, m = map(int, input().split())

# li = []
# for i in range(n):
#     li.append(sorted(list(map(int, input().split())))[0])

# print(sorted(li)[n - 1])
# sorted()를 쓰지 않아도 되는 로직에서 사용해버렸다

##### 두번째 로직 #####
n, m = map(int, input().split())

li = []

for i in range(n):
    li.append(min(list(map(int, input().split()))))

print(max(li))
# mix()와 max()함수 기억하기!
