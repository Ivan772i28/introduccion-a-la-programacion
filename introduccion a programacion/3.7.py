
n1 = int(input("ingresa el primer numero :"))
n2 = int(input("ingresa el segundo numero :"))
if n1<n2:
		menor = n1
		mayor = n2
else:
		menor = n2
		mayor = n1
for i in range(menor,mayor+1):
    if i!=mayor:
        print(i,end=", ")
    else:
        print(i)