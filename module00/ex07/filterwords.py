import sys

if len(sys.argv) != 3:
    sys.exit("ERROR")
try:
    s = sys.argv[1]
    num = int(sys.argv[2])
except:
    sys.exit("ERROR")
lst = s.split(" ")
words = []
for i in lst:
    res = "".join(j for j in i if j.isalpha())
    if len(res) > num:
        words.append(res)
print(words)