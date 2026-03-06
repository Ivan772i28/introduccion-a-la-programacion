if __name__ == '__main__':
	print("ingresa el tipo de membresia que tienes")
	tipo_m = input()
	print("Ingresa el gasto")
	gastofn = float(input())
	if tipo_m in "A-a-B-b-C-c":
		descuento = 0.1
	
		if tipo_m=="B" or tipo_m=="b":
			descuento = 0.15
		else:
			if tipo_m=="C" or tipo_m=="c":
				descuento = 0.2
			else:
				descuento = 0
	gastofn = gastofn-(gastofn*descuento)
	print("el precio final a pagar es : ",gastofn)