# hipótesis de Lothar Collatz. Tendencia de los números positivos al valor 1
# Si es par se divide por 2, si es impar se multiplica por 3 y se le suma 1
c0 = int(input("Ingrese un número"))
pasos = 0

while c0 > 1:
    if c0 % 2 == 0:
        c0 //= 2
        pasos += 1
        print(c0)
    elif c0 % 2 == 1:
        c0 = c0 * 3 + 1
        print(c0)
        pasos += 1
print("Pasos: ", pasos)
        

    
    