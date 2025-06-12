def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

# Programa principal
numero = int(input("Ingrese un numero entero positivo: "))

if numero <= 0:
    print("Ingrese un numero")
else:
    binario = decimal_a_binario(numero)
    print(f"El numero {numero} en binario es: {binario}")
