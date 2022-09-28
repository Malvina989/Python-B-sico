# Crear lista vacía
Beatles = []
print("Paso 1:", Beatles)

# append para agregar miembros
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# usuario ingrese miembros restantes con for y append
for i in range(2):
    Beatles.append(input("Ingrese miembros: Stu Sutcliffe, Pete Best"))
print("Paso 3:", Beatles)

# borrar a Stu y Pete
del Beatles[-1]
del Beatles[-1]
print("Paso 4:", Beatles)

# insertar a Ringo Starr al principio de la lista
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))
