# Utilizando un bucle “while”, elaborar un código
# que imprima en pantalla cada uno de los
# elementos de una lista y simultáneamente los
# elimine, hasta quedar vacía.

lista = [44, True, "Hola", 33.8, 15, "Chau"]
i = 0

while i < len(lista):
    print(lista[i])
    del lista[i]
    i+=i
print("La lista esta vacía: ", lista)