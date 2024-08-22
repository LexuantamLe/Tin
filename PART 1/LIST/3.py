n = int(input("Nhap tong so trong list A"))
a=[]
b=[]
for i in range(n):
   a.append(str(input("Day A So "+str(i+1)+": ")))
a = a[::-1]
for i in range(n//2+1):
    b.append(a[i])
print(b)
     

