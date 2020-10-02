import re


def task1(string):
    mas = [i for i in string.split()]
    result = []
    temp = mas[0]
    for i in mas[1:]:
        if temp[-1] == i[0] and re.match(r'[A-Za-z]', temp[-1]):
            result.append("{} {}".format(temp, i))
        temp = i
    return result if result else ""


def task2(path):
    file = open(path, "r")
    arr = file.readlines()
    file.close()
    file = open(path, "w")
    for i in arr:
        for j in (i.split()):
            if j == "public":
                file.write("private")
            else:
                file.write(j)
            file.write(" ")
        file.write("\n")
    file.close()
    return path


def task3(path):
    file = open(path, "r")
    mas = []
    a = file.readline()
    while a != '':
        mas.append([int(i) for i in a.split()])
        a = file.readline()
    for i in range(len(mas)):
        for j in range(i, len(mas[i])):
            mas[i][j], mas[j][i] = mas[j][i], mas[i][j]
    return mas


def task4(path1, path2):
    patt = re.compile(r"as\d+")
    file1 = open(path2, "w")
    with open(path1, "r") as f:
        for line in f:
            for i in re.findall(patt, line):
                file1.write(i)
    file1.close()
    return path2


def task5(string):
    patt = re.compile(r"\d+")
    result = re.findall(patt, string)
    temp = ""
    for i in result:
        if len(i) > len(temp):
            temp = i
    return temp


if __name__ == "__main__":
    task3("txt.txt")