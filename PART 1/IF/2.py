# a=[]
# for i in range(3):
# 	a.append(input(str(i+1)+" :"))
# print(sorted(a))

a = int(input('Num a:'))
b = int(input('Num b:'))
c = int(input('Num c:'))

if c<b and c<a:
	a,c = c,a 
if b<a and b<c:
	a,b=b,a 
if b>c:
	b,c=c,b
print(a,b,c)