frutas=["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta,len(fruta))
    contador=0
    for letra in fruta:
        if letra.lower() in "aeiouéáíóú":
            contador+=1
    print("Número de vocales en", fruta, "es:", contador)