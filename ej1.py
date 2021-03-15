#Desarrolle un programa en el cual permita registrar 10 alumnos con nombre y numero de
#carné y los almacene en una tupla, al finalizar el registro de los alumnos se deben mostrar
#por pantalla todos los alumnos registrados.
def ej1():

    print()
    alumno = input("Nombre del alumno: ")
    carnet = int(input("Dame el numero de carnet del alumno: "))
    print()

    return (alumno, carnet)

nombre1=ej1()
nombre2=ej1()
nombre3=ej1()
nombre4=ej1()
nombre5=ej1()
nombre6=ej1()
nombre7=ej1()
nombre8=ej1()
nombre9=ej1()
nombre10=ej1()

print([nombre1], [nombre2], [nombre3], [nombre4], [nombre5], [nombre6], [nombre7], [nombre8], [nombre9], [nombre10])
