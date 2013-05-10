#marcelo minay
#Problema 4. Coeﬁciente del demonio 2.0



#Funcion que determina las k combinaciones posibles de un set
def combinatoria2(conjunto,k):
    import itertools    #librería que contiene la funcion combinations

    #Se declara una lista vacia
    lista_aux=[]

    #Ciclo que va obteniendo las diferentes combinaciones posibles (sin repetir)
    for combinacion in itertools.combinations(conjunto,k): #función que determina todas las combinaciones posibles dentro del set
        lista_aux.append(combinacion) #Agrega a la lista una combinación encontrada a la vez
    

    return lista_aux #Devuelve todas las combinaciones del set agregadas a la lista


conjunto = set() #Declarar set vacio

#Se le pide al usuario que igrese un número mayor o igual a 1 en caso de que no siga la instrucción se le vuelve a pedir.
while True:
    cantidad=int(input("Ingrese la cantidad de elementos que desea ingresar al conjunto "))

    
    #Comprueba que el entero ingresado sea mayor a 1
    if cantidad < 1:
        print("Error, se ha ingresado un valor invalido")
    else:
        #Se le pide al usuario los datos que debemos combinar (tantos datos como dijo antes que debían ser
        for i in range(0,cantidad):
            dato=input("Ingrese un elemento: ")
            conjunto.add(dato) 		#Se agrega el dato señalado por el usuario al set
        break

#Se le solicita k al usuario hasta que sea mayor a 0 y menor a cantidad
while True:
    print("Ingrese un 'k' mayor a 0 y menor o igual a",cantidad)
    k=int(input())

    if k > cantidad or k < 1:
        print("Error, k no valido")
    else:
        break
    

#Variable tipo lista que recibe todas las combinaciones posibles de un set determinado por el usuario
combinaciones=combinatoria2(conjunto,k)

#Imprime la lista con todas las combinaciones posibles del set
for dato in combinaciones:
    print(dato,"\n")
