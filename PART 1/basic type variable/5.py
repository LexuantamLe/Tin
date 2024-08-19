n=int(input("Total Item Will Be Listed ?:"))
a=[]
for i in range(1,n+1):
    i = int(input("Item "+str(i)))
    a.append(i)
if a[0]%2==0:
    for i in range(0,n):
        if a[i] %2 == 0:
            if i+1 < int(len(a)):
                if a[i+1] %2 == 0:
                    print("FALSE")
                    exit()
        if a[i] %2 != 0:
            if i+1 < int(len(a)):
                if a[i+1] %2 != 0:
                    print("FALSE")
                    exit()
else:
    for i in range(0,n):
        if a[i] %2 != 0:
            if i+1 < int(len(a)):
                if a[i+1] %2 != 0:
                    print("FALSE")
                    exit()
        if a[i] %2 == 0:
            if i+1 < int(len(a)):
                if a[i+1] %2 == 0:
                    print("FALSE")
                    exit()
print("TRUE")
