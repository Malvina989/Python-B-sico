paises = {"ar": "Argentina",
"es": "España",
"us": "Estados Unidos",
"fr": "Francia"
}

while True:
    valor = input("Ingrese clave")
    if valor == "salir":
        break
    try:
        print(paises[valor])
    except KeyError:
        print("La clave ingresada no corresponde a un país") 
        
