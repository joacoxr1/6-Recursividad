def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

numero = int(input("Ingresa un numero entero: "))

# Validar entrada y calcular los factoriales
if numero < 1:
    print("Ingresa un numero mayor o igual a 1.")
else:
    print(f"Factoriales del 1 al {numero}:")
    for i in range(1, numero + 1):
        print(f"{i} = {factorial(i)}")
