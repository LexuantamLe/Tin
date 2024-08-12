a=int(input("Number A="))
b=int(input("Number B="))
i=1
##
if a>b:
	n=b
if a<b:
	n=a
##Maximum
while i<n+1:
	if a%i == 0 and b%i==0:
		maxi=i 
	i=i+1
##Minimum
m=n
while m<a*b+1:
	m=m+1
	if m%a==0 and m%b==0:
		print("HSC:",m*maxi)
		#EXIT
		pause=input("Enter To Exit")
		exit()
