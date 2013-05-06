def ganador_cachipun(jugadores):
	if len(jugadores)!=4:
		Exception("Error la cantidad de datos ingresados no es válida")
		print("pajarito")
	if jugadores[0][1] == 'r' or jugadores[0][1] == 'p' or jugadores[0][1] == 't':
		if jugadores[1][1] == 'r' or jugadores[1][1] == 'p' or jugadores[1][1] == 't':
			
		else
			Exception("error jugador 2 cometio jugada no válida")
	else:
		print("perrito")
		Exception("error jugador 1 cometio jugada no válida")
	
	
	return 0

jugadores= [[input("Ingrese el nombre del primer jugador "), input("Ingrese la Jugada primer ")], [input("Ingrese el nombre del segundo jugador "), input("Ingrese la Jugada jugador ")]]
ganador_cachipun(jugadores)
print(jugadores[0][1],jugadores[1][1])
