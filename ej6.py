#Desarrolle un programa que permita registrar 8 jugadores de videojuegos (gamers) con su
#respectiva edad, en cada registro se debe validar la edad del alumno para clasificarlo según
#la siguiente tabla de clasificación:
#•	Novato = entre 14 y 16 años
#•	Experto = entre 17 y 20 años
#•	Super Experto = mayores a 20 años
def ej6():
    novato=[]
    experto=[]
    super_experto=[]
    for x in range(8):
        jugador = input('Escriba el NOMBRE del jugador: ')
        edad = int(input('Digite la EDAD del jugador: '))
        if edad < 14:
            print("EDAD NO VALIDA: La EDAD debe ser de 14 en adelante")
            edad = int(input('Ingrese la EDAD del jugador: '))
        elif edad >= 14 and edad <= 16:
            novato.append((jugador,edad))
        elif edad > 16 and edad <= 20:
            experto.append((jugador,edad))
        elif edad > 20:
            super_experto.append((jugador,edad))
    print("1. Novato")
    print("2.Experto")
    print("3.Super Experto")
    elige=int(input('Seleccione la categoria: '))
    if elige==1:
        print(novato)
    elif elige==2:
        print(experto)
    elif elige==3:
        print(super_experto)
ej6()