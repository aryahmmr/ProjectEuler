#x1=1
#x2=1
#tot=0
x1, x2, tot = 1, 2, 0
i=0
while x1<=4e6:
#	print(f"these are the variables x1={x1} and x2={x2}\n")
	temp1=x1
	if x2 % 2 == 0:
		tot+=x2
	#x1=x2
	#x2=temp1+x2
	x1, x2 = x2, x1+x2

print(f"this is the total: {tot}")
