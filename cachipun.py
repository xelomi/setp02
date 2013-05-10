#marcelo minay
#realizar una función que determine el ganador del juego cachipun


def ganador_cachipun(jugadores):     #r=piedra t=tijera p=papel
	if len(jugadores)!=4:
		Exception("Error la cantidad de datos ingresados no es válida")
	if jugadores[0][1] == 'R' or jugadores[0][1] == 'P' or jugadores[0][1] == 'T':        #comprueba quien gana o si los usuarios cometieron una jugada inválida
		if jugadores[1][1] == 'R' or jugadores[1][1] == 'P' or jugadores[1][1] == 'T':
			if (jugadores[0][1] == 'R' and jugadores[1][1] == 'T') or (jugadores[0][1] == 'P' and jugadores[1][1] == 'R') or (jugadores[0][1] == 'T' and jugadores[1][1] == 'P'):
				print(jugadores[0][0]," gana ", jugadores)
			if jugadores[1][1] == 'R' and jugadores[0][1] == 'T' or jugadores[1][1] == 'P' and jugadores[0][1] == 'R' or jugadores[1][1] == 'T' and jugadores[0][1] == 'P':
				print(jugadores[1][0]," gana ", jugadores)
			if jugadores[0][1]==jugadores[1][1]:
				print(jugadores[0][0]," gana ", jugadores)
		else:
			Exception("error jugador 2 cometio jugada no válida")
	else:
		Exception("error jugador 1 cometio jugada no válida")
	return 0

jugadores= [[input("Ingrese el nombre del primer jugador "), input("Ingrese la Jugada primer ")], [input("Ingrese el nombre del segundo jugador "), input("Ingrese la Jugada jugador ")]]
jugadores[0][1]=jugadores[0][1].upper
jugadores[1][1]=jugadores[1][1].upper
ganador_cachipun(jugadores)
