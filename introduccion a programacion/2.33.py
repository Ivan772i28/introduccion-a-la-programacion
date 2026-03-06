

nmes= int(input("ingesa el número de mes: "))
ndia=int(input("Ingresa el número de día: "))
if nmes==1 or nmes==3 or nmes==5 or nmes==7 or nmes==8 or nmes==10 or nmes==12:
    # Meses con 31 días
    if ndia>=1 and ndia<=31:
        print("Fecha válida")
    else:
        print("Día inválido")
elif nmes==4 or nmes==6 or nmes==9 or nmes==11:
    # Meses con 30 días
    if ndia>=1 and ndia<=30:
        print("Fecha válida")
    else:
        print("Día inválido")
elif nmes==2:
    # Febrero (sin considerar años bisiestos)
    if ndia>=1 and ndia<=28:
        print("Fecha válida")
    else:
        print("Día inválido")
else:
    print("Mes inválido") 
