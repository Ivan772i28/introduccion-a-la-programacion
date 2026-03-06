horas = int(input("Ingrese las horas trabajadas: "))

if horas <= 40:
    salario = horas * 20
else:
    horasExtras = horas - 40
    salario = (40 * 20) + (horasExtras * 25)

print(f"El salario semanal es: ${salario:,.2f}")