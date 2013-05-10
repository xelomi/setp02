#Marcelo mMinay
#actividad: Realizar una función que sume todos los elementos de una tupla.

def sumall(tupla):
	suma=0
	for valor in tupla:
		suma=suma+valor
		
	return suma;
	
	
	


#se llena la tupla, se llama la función y se prueba que funcione
tuplacs=(1,2,3,4,5,6,7,6)
valors=sumall(tuplacs)
print (valors)

