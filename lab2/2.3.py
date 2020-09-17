path = r"C:\Users\Anton\Desktop\test.txt"
file = open(path, "r")
mas = []
a = file.readline()
while a != '':
    mas.append([int(i) for i in a.split()])
    a = file.readline()
print(mas)
for i in range(len(mas)):
    for j in range(i, len(mas[i])):
        mas[i][j], mas[j][i] = mas[j][i], mas[i][j]
for i in range(len(mas)):
    for j in range(len(mas[i])):
        print(mas[i][j], end=" ")
    print("\n")