# 1 - El usuario ingresa el tamaño de la coleccion de datos
# 2 - Se le debe pedir al usuario que ingrese tantos numero de acuerdo al tamaño de la coleccion
# Al finalizar la carga, mostrar por pantalla que si es multiplo de 3 imprimir "Fizz", si es multiplo de 5 imprimir "Buzz" y para los que son multiplos de 3 y de 5 imprimir "FizzBuzz" sino ,mostrar el valor

listaLong = int(input("Ingrese cantidad de datos a ingresar"))
lista = []

for i in range (0, listaLong):
    dato = int(input("Ingrese datos"))
    lista.append(dato)
print(lista)

for i in range(0, len(lista)):
    if lista[i] % 5 == 0 and lista[i] % 3 == 0:
      print("FizBuzz")
    elif lista[i] % 3 == 0:
      print("Fizz")
    elif lista[i] % 5 == 0:
      print("Buzz")
    else:
      print(lista[i])



