
def comparar_manos(p1,p2):
	mazo={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}
	punto1=0;
	punto2=0;
	for carta in p1:
		punto1=punto1+mazo[carta]
	for carta in p2:
		punto2=punto2+mazo[carta]
		
		
	if punto1 >= punto2:
		print("El jugador 1 gana")
	else:
		print("El jugador 2 gana")	
		
		

p1=(input("perrito"),input("perrito"),input("perrito"),input("perrito"),input("perrito"),input("perrito"),input("perrito"))
p2=(input("perrito"),input("perrito"),input("perrito"),input("perrito"),input("perrito"),input("perrito"),input("perrito"))

comparar_manos(p1,p2)
