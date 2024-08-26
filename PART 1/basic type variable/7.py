f = open("DATA.txt","r",encoding = "UTF-8")
n = int(f.read())
f.close()

a=(n-1)+(n-2)

f = open("KQ.txt", 'w',encoding = "UTF-8")
f.write(str(a))
f.close()
