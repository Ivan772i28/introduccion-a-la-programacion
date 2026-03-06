numeros = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10] 
 
for numero in numeros: 
    if numero % 2 == 0: 
        print(f"Encontrado número par: {numero}") 
        break 

def encontrar_primer_par(numeros): 
    for numero in numeros: 
        if numero % 2 == 0: 
            continue 
        print(f"Número impar encontrado: {numero}")
    
encontrar_primer_par(numeros)