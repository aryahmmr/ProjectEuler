x1=3
x2=5
tot=0
i=0
#while i < 1000:
for i in range (1000):  
	if i % 3 == 0 or i % 5 == 0:
		 tot+=i
#	i+=1

print(f"the total is: {tot}")
