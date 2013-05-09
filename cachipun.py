def ganador_cachipun(jugadores):     #r=piedra t=tijera p=papel
	if len(jugadores)!=4:
		Exception("Error la cantidad de datos ingresados no es válida")
	if jugadores[0][1] == 'r' or jugadores[0][1] == 'p' or jugadores[0][1] == 't':
		if jugadores[1][1] == 'r' or jugadores[1][1] == 'p' or jugadores[1][1] == 't':
			if (jugadores[0][1] == 'r' and jugadores[1][1] == 't') or (jugadores[0][1] == 'p' and jugadores[1][1] == 'r') or (jugadores[0][1] == 't' and jugadores[1][1] == 'p'):
				print(jugadores[0][0]," gana ", jugadores)
			if jugadores[1][1] == 'r' and jugadores[0][1] == 't' or jugadores[1][1] == 'p' and jugadores[0][1] == 'r' or jugadores[1][1] == 't' and jugadores[0][1] == 'p':
				print(jugadores[1][0]," gana ", jugadores)
			if jugadores[0][1]==jugadores[1][1]:
				print(jugadores[0][0]," gana ", jugadores)
		else:
			Exception("error jugador 2 cometio jugada no válida")
	else:
		Exception("error jugador 1 cometio jugada no válida")
	return 0

jugadores= [[input("Ingrese el nombre del primer jugador "), input("Ingrese la Jugada primer ")], [input("Ingrese el nombre del segundo jugador "), input("Ingrese la Jugada jugador ")]]
ganador_cachipun(jugadores)
