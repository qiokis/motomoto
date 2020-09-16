import re
patt = re.compile(r"as\d")
file = open("C:\\Users\\Anton\\Desktop\\test.txt", "r")
file1 = open("C:\\Users\\Anton\\Desktop\\test1.txt", "w")
mas = file.readline().split()
while mas:
    for i in mas:
        if re.match(patt, i):
            file1.write(i+" ")
    mas = file.readline().split()
file1.close()