import re
string = "asdad21dvo2n352vn0620352385"
patt = re.compile(r"\d+")
result = re.findall(patt, string)
temp = ""
for i in result:
    if len(i) > len(temp):
        temp = i
print(i)