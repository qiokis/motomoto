import re
patt = re.compile(r"as\d+")
file = open(r"C:\Users\Anton\Desktop\test.txt", "r")
file1 = open(r"C:\Users\Anton\Desktop\test1.txt", "w")
mas = file.readline()
with open(r"C:\Users\Anton\Desktop\test.txt", "r") as f:
    for line in f:
        for i in re.findall(patt, line):
            file1.write(i + " ")
file1.close()
