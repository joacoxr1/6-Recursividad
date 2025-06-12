def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

if exponente < 0:
    print("El exponente debe ser un numero entero")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")
