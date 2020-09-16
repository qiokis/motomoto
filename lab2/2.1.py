mas = [i for i in input().split()]
temp = mas[0]
for i in mas[1:]:
    if temp[-1] == i[0]:
        print(temp, i)
    temp = i