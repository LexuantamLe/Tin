n = int(input("Nhap tong so trong list"))
a=[]
for i in range(n):
   a.append(int(input("So "+str(i+1)+": ")))
print(a[::-1])
