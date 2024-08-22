n = int(input("Nhap tong so trong list A"))
f=[1,1]
a=f[0]
b=f[1]
for i in range(2,n+1):
    c = a+b
    f.append(c)
    a=b 
    b= c 
print(f)
