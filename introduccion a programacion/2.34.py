res="si"
while res.lower()=="si":
    print("ingresa el primer valor")
    n1 = float(input())
    print("ingresa el el caracter +, -, *, /) ")
    operador = input()
    print("ingresa el segundo valor")
    n2 = float(input())
    if operador=="+":
        resultado = "el resultado de la suma es: " + str(n1+n2)
    elif operador=="-":
        resultado = "el resultado de la resta es: " + str(n1-n2)
    elif operador=="*":
        resultado = "el resultado de la multiplicacion es: " + str(n1*n2)
    elif operador=="/":
        resultado = "el resultado de la division es: " + str(n1/n2)
    else:
        resultado="ingresa un caracter valido"
    print(resultado)
    res=input("¿deseas realizar otra operacion? (si/no): ")
