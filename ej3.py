#Desarrolle un programa en el cual permita registrar 10 países con sus respectivas capitales
#utilizando diccionarios.
def ej3():
    paises={}
    for x in range(10):
        pais=input("Ingrese el nombre de un pais:")
        capital=input("Ingrese la capital:")
        paises[pais] = capital
    return paises

def imprimir(paises):
    print("Listado del diccionario completo")
    for pais in paises:
        print(pais, paises[pais])
paises=ej3()
imprimir(paises)


