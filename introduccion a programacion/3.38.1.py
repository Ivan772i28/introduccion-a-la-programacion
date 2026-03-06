
nummayor = int(input("ingresa el numero: "))
num = nummayor
while num!=0:
	if num>nummayor:
		nummayor = num
	
	num = int(input("ingresa el numero: "))
print("el numero mayor es: ",nummayor)
