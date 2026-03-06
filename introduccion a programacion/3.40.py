suma = 0
contador = 0
ning=float(input("ingresa un numero(ingresa negativo si desea terminar)\n"))

while ning>=0:
	suma = suma+ning
	contador = contador+1
	ning=float(input("ingresa un numero(ingresa negativo si desea terminar):  "))
if contador>0:
	promedio = suma/contador
	print("la media es: ",promedio)
else:
	print("no se ingresaron numeros positivos")

