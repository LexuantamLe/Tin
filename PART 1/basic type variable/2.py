st=str(input("Input String:"))
st = st.replace("  "," ")
st_convert=""
if st[0] == " ":
    for i in range(1,int(len(st))):
        if st[i] == " " and st[i-1] == " ":
            pass
        else:
            st_convert=st_convert+st[i]
print(st_convert)
print("CHARACTER (HAVE SPACE): "+str(len(st_convert)))
print("CHARACTER (NO SPACE): "+str(len(st_convert.replace(" ",""))))
