#marcelo minay
#Funcion que determina si en el juego ganas, pierdes o continuas.


from random import * #Libreria que contiene función que genera números al azar 

def scrap(pierdes,ganas):
    jugar = True #Se repetirá esta función mientras se mantenga en true

    lanzamiento = (randint(1,6),randint(1,6))   #Se lanzan los dados 
    print("Lanzamiento: "+ str(lanzamiento))    #Se le dan a conocer al usuario sus dados
    if lanzamiento in pierdes:  #Si la combinación que obtuvo se encuentra en la lista "pierdes", pierde el usuario
        print("Pierdes")
    else:
        if lanzamiento in ganas:    #Si la combinación que obtuvo se encuentra en la lista "ganas", gana el usuario
            print("Ganas")
        else:                   #Si el lanzamiento no está ni en "ganas" ni "pierdes", el usuario obtiene un punto
            print("Punto")
            
            puntaje = lanzamiento[0] + lanzamiento[1]   #Se suman los dados que se obtuvieron
            
            while jugar:   #Este ciclo se repite mientras el usuario vaya consiguiendo el puntaje, gane o pierda
                
                lanzamiento_punto = (randint(1,6),randint(1,6)) #Se lanza nuevamente
               
                print("Lanzamiento: "+ str(lanzamiento_punto))  #Notifica al usuario el nuevo lanzamiento

                if puntaje == 7:    #Si se llega a puntaje 7 pierdes
                    print("Pierdes")
                    jugar = False
                else:
                    if lanzamiento_punto == lanzamiento:    #Si consigues la misma suma 2 veces ganas.
                        print("Ganas")
                        jugar = False
        
        



dados = [] #Se guardaran todas las combinaciones posibles con 2 dados en esta lista.

for i in range(13):
    dados.append(set())  #Se agregan 12 espacios vacios (se coloca hasta 13 porque es excluyente)

#Generar todas las combinaciones posibles de lanzamientos
#La suma de los dados es el indice de la lista que corresponden a un set
for i in range(1,7):
    for j in range(1,7):
        dados[i+j].add((i,j))

pierdes = dados[2]|dados[3]|dados[12] #Pierdes

ganas = dados[7]|dados[11]    #Ganas si ejecutas estos lanzamientos

punto = dados[4]|dados[5]|dados[6]|dados[8]|dados[9]|dados[10] #Ganas un punto

scrap(pierdes,ganas)
