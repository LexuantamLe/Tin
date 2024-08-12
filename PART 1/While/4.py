n = int(input("How many numbers ?: "))
a = []
k = 0
while k < n:
    a.append(int(input("Number "+str(k+1)+": ")))
    k += 1
maxi = a[0]
i = 1
while i < len(a):
    while a[i] != 0:
        maxi, a[i] = a[i], maxi % a[i]
    i += 1
print("RESULT: ", maxi)
