f = open("inp.txt","r",encoding = "UTF-8")
n = int(f.read())
f.close()

f = open("out.txt", 'w',encoding = "UTF-8")
for i in range(2, n + 1):
    f.write(str(i) + "\n")
f.close()
