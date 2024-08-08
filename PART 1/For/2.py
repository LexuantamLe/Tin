a = []
s= 0
n = int(input('Number: '))
# run 2 -> n (1 is exception)
for i in range(1,n):
	#run 1 -> j
	for j in range(1,i+1):
		# j%i = 0 
		if i%j == 0:
			s=s+j
			if s == i:
				a.append(i)
	s=0
			
print(a)

