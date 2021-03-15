#Desarrolle un programa en el cual permita registrar 10 marcas de productos, con nombre y
#código de producto, estos deben ser almacenados en listas. Al finalizar el registro debe
#mostrar todos los productos registrados.
def ej2():
    marca = []
    codigo = []
    for x in range(10):
        nombre = input('Escriba la MARCA del producto')
        marca.append(nombre)
        nombrep = input('Escriba el NOMBRE del producto')
        codigop = input('Digite el CODIGO del producto')
        codigo.append([nombrep,codigop])
    for x in range(10):
        print(marca[x],codigo[x][0],codigo[x][1])
ej2()
