st=str(input("Input String:"))
if len(st)%2 == 0 :
    for i in range(int(len(st)/2)):
        if st[i] != st[len(st)-1-i]:
            print("Not Mirror String")
            exit()
    print("Mirror String")
else:
    print("Not Mirror String")
