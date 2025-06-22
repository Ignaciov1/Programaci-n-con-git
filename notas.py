def pedir_cantidad_notas():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de notas:"))
            if cantidad > 1:
                break
            else:
                print("Debes ingresar al menos 1 nota.")
        except:
            print("Valor invalido. Solo puedes ingresar numeros.")
    return cantidad

cantidad = pedir_cantidad_notas()
print(cantidad)



# add codigo oleivac
print(cantidad)