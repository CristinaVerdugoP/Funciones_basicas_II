#-----------CUENTA REGRESIVA----------------
def cuenta_regresiva(numero):
    lista_vacia = []
    while numero+1>0:
        numero-=1
        lista_vacia += [numero+1]
    print("\nResultado de la cuenta regresiva es:", lista_vacia)
cuenta_regresiva(5)

#-------------IMPRIMIR Y DEVOLVER----------------

def imprimir_devolver(imprimir,devolver):
    print("\nResultado de imprimir y devolver: ")
    print("Se imprime",imprimir)
    return devolver

print("Se devuelve:",imprimir_devolver(1,2))

#-------------PRIMERO MAS LONGITUD--------------

def primero_longitud(lista):
    x = lista[0] + len(lista)
    return x
print("\nResultado de Primero mas longitud")
print("La suma será: ", primero_longitud([1,2,3,4,5]))

#---------VALORES MAYORES QUE EL SEGUNDO----------
def mayor_segundo(lista_entrada):
    lista_vacia2 = []
    contador = 0
    for i in lista_entrada:
        if i > lista_entrada[1]:
            lista_vacia2.append(i)
            contador = contador + 1
        else:
            pass
    print("\nResultado de valores mayores que el segundo")
    print("total de numeros mayores:", contador)
    return lista_vacia2

print("Lista de los numero mayores que el segundo:", mayor_segundo([5,3,4,6,1,9,10]) )

#------------ESTA LONGITUD, ESE VALOR-------------

def longitud_valor(longitud,valor):
    lista_vacia3 = []
    for i in range(0,longitud):
        lista_vacia3.append(valor)
    return lista_vacia3

print("\nResultado de Esta longitud, ese valor: ", longitud_valor(4,9))