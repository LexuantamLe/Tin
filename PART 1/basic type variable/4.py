n=int(input("Total Item Will Be Listed ?:"))
a=[]
b=[]
for i in range(1,n+1):
    i = int(input("Item "+str(i)))
    a.append(i)
    b.append(i)
a.sort()
for i in range(int(len(a))):
    if a[i] != b[i]:
        print("FALSE")
        exit()
print("TRUE")
