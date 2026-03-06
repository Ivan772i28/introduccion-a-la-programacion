nummayor = -9999
num = int(input("ingresa el numero "))
while num!=0:
		if num>nummayor:
			nummayor = num
		print("ingresa el numero")
		num = int(input())
print("el numero mayor es",nummayor)

