def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

posicion = int(input("Ingresa una posicion: "))

if posicion < 0:
    print("ingresa un numero mayor o igual a 0.")
else:
    print(f"Fibonacci hasta la posicion {posicion}:")
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci(i)}")
