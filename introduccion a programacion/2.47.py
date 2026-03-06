nombre=input("Ingresa tu nombre :")
for i in range(len(nombre)):
    print(nombre[:i+1])
print("-----------")
for i in range(len(nombre)-1, -1, -1):
    print(nombre[i:])
print("-----------")
centro=len(nombre)//2
for i in range(centro+1):
    print(nombre[centro-i:centro+i+1])