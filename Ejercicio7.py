def contar_bloques(num):
    if num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)


print(contar_bloques(1)) 
print(contar_bloques(2))  
print(contar_bloques(4))  
