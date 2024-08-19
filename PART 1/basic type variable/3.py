st=str(input("Input String:"))
st_c=""
for i in range(int(len(st))):
    if st[i] in "0123456789":
        st_c=st_c+st[i]
        if i+1 < int(len(st)) and st[i+1] not in "0123456789":
            st_c=st_c+"+"
print(st_c)
print(eval(st_c))
