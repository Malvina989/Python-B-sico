# Crear un bucle que almacene en una variable la
# suma de todos los elementos numéricos de una
# lista, con excepción del último.

lista = [4, 8, "Ana", -7, "Jorge", True, 15, 13]
resultado = 0

for i in range(0, len(lista)-1):
    if type(lista[i]) is int:
        resultado +=  lista[i] 
   
    
print(resultado)