#Desarrolle un programa que permita registrar 8 cursos con la respectiva nota entre 50 y 100
#puntos, al finalizar el registro el sistema debe mostrar únicamente los cursos cuya nota
#representa aprobación del curso ( 61 o superior ). Si el numero ingresado es menor a 50 el
#programa debe mostrar mensaje de error y permitir volver a ingresar el registro.
def ej5():
    ganados=[]
    for x in range(10):
        curso = input("Escriba el nombre del curso: ")
        nota = int(input("Digite la nota: "))
        if nota >50:
            if nota >61:
                ganados.append((curso,nota))
        else:
            print("Error, digite nuevamente la nota: ")
            nota = int(input("Digite nota: "))
    print("Los curso ganados son: ")
    print(ganados)
ej5()
