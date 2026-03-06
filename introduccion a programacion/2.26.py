cal1 = float(input("Ingrese la primera calificación: "))
cal2 = float(input("Ingrese la segunda calificación: "))
cal3 = float(input("Ingrese la tercera calificación: "))

promedio = (cal1 + cal2 + cal3) / 3

print("El promedio es:", promedio)

if promedio >= 70:
    print("El estudiante APROBÓ")
else:
    print("El estudiante REPROBÓ")