def suma_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + suma_digitos(num // 10)


print(suma_digitos(1234)) 
print(suma_digitos(9))    
print(suma_digitos(305)) 
