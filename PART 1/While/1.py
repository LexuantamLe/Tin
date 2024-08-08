while True:
	n = int(input('N (0<N<1000) = '))
	i=0
	s=0
	if n>0 and n<1000:
		while i<n:
			s=s+i
			i=i+1
		print("Sum: x < "+str(n)+" = "+str(s))
		print("**Sum: x =< "+str(n)+" = "+str(s+n))
		exit()
	else:
		pass

