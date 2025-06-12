def contar_digito(num, digito):
    if num == 0:
        return 0
    elif num % 10 == digito:
        return 1 + contar_digito(num // 10, digito)
    else:
        return contar_digito(num // 10, digito)
        
print(contar_digito(12233421, 2)) 
print(contar_digito(5555, 5))     
print(contar_digito(123456, 7))    
