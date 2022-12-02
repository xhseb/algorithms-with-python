n, k = map(int, input().split())

li = []
for i in range(2, n + 1):
    li.append(i)

count = 0

while (count != k):
    min = li[0]
    li.remove(min)
    count += 1
    if count == k:
        print(min)
        break
    for l in li:
        if l % min == 0:
            li.remove(l)
            count += 1
            if count == k:
                print(l)
                break

#NOTE - remove를 사용하기보다 리스트 인덱스 자체를 사용하는 것이 시간복잡도가 줄어든다!
# 인자 세개 받는 range 기억해두기 
N, K = map(int, input().split())

cnt = 0

li = [True] * (N + 1)
for i in range(2, len(li) + 1):
    for j in range(i, N+1, i):
        if li[j] == True:
            li[j] = False
            cnt = cnt + 1
            if cnt == K:
                print(j)
                break