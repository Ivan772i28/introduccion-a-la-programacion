compra=float(input("ingrese el valor de la compra :"))
if compra>15000:
    descuento=compra*0.10
else: 
    descuento=compra*0.05
preciofn=compra-descuento
print("el descuento es: ",descuento)
print("el precio final es de :",preciofn)