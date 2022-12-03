list = input()

s = 0
bool = True
li = []

for i in range(len(list)):
    if bool and list[i] == '<':
        e = i - 1
        while s <= e:
            li.append(list[e])
            e -= 1
        s = i
        bool = False
    elif bool and i == len(list) - 1:
        e = i
        while s <= e:
            li.append(list[e])
            e -= 1
    elif not bool and list[i] == '>':
        bool = True
        while s <= i:
            li.append(list[s])
            s += 1
    elif bool and list[i] == ' ':
        e = i - 1
        while s <= e:
            li.append(list[e])
            e -= 1
        li.append(' ')
        s = i + 1

for x in range(len(li)):
    if x != len(li) - 1:
        print(li[x], end="")
    else:
        print(li[x])
