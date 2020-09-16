path = "C:\\Users\\Anton\\Desktop\\test.java"
file = open(path, "r")
arr = file.readlines()
file.close()
file = open(path, "w")
print(arr)
for i in arr:
    for j in (i.split()):
        if j == "public":
            file.write("private")
        else:
            file.write(j)
        file.write(" ")
    file.write("\n")