# escribir un programa que lea la cantidad de bloques que tienen los constructores,
# y generar la altura de la pirámide con capas completasque se puede construir 
# utilizando estos bloques.
blocks = int(input("Ingresa el número de bloques: "))
height = 0
use = 0

while blocks > use:
    use += 1
    blocks -= use
    height += 1
    
    
print("La altura de la pirámide:", height)
