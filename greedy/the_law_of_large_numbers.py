n, m, k = map(int, input().split())
li = list(map(int, input().split()))

# 입력받은 수들 내림차순으로 정렬하기
li.sort(reverse=True)

# 큰 수가 한 개일 때와 두 개일 때를 분리함
if (li[0] == li[1]):
    print(li[0] * m)
else:
    print(m // (k + 1) * (k * li[0] + li[1]) + m % (k + 1) * li[0])


#NOTE - greedy 최대한 하나의 식으로 일반화할 수 있도록 고민해보자!
# count = int(m / (k + 1)) * k
# count += m % (k + 1)

# result = 0
# result += (count) * first # 가장 큰 수 더하기
# result += (m - count) * second # 두 번째로 큰 수 더하기

# print(result) # 최종 답안 출력