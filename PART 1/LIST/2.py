n = int(input("Nhap tong so trong list A"))
m = int(input("Nhap tong so trong list B"))
a=[]
b=[]
a1=[]
a2=[]
for i in range(n):
   a.append(int(input("Day A So "+str(i+1)+": ")))
for i in range(m):
   b.append(int(input("Day B So "+str(i+1)+": ")))
k = int(input("So chen trong a"))
for i in range(len(a)):
    a1.append(a[i])
    if a[i] == k:
        for j in range(1,len(a)-i):
            a2.append(a[j+i])
        print(a1+b+a2)
        exit()

