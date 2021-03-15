#Desarrolle un programa que pueda recorrer el diccionario del ejercicio anterior y los muestre
#por pantalla todos los países con sus respectivas capitales.
def imprimir(paises):
    print("Listado del diccionario completo")
    for pais in paises:
        print(pais, paises[pais])
paises=cargar()
imprimir(paises)