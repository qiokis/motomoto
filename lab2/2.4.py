import re
patt = re.compile(r"\d\w+")
file = open("C:\\Users\\Anton\\Desktop\\test.txt", "r")
file1 = open("C:\\Users\\Anton\\Desktop\\test1.txt", "w")
mas = file.readline().split()
for i in mas:
    if re.match(patt, i):
        file1.write(i)
file1.close()