#--------------------------------------------------PREGUNTA 1-----------------------------------------------------------
#Modificar el juego 3 en raya, para que se aplique la misma lógica,
#pero en un tablero de 5x5 (gana el primero que logra enlazar 3 marcas similares, horizontales, verticales o diagonales).

#Tres En Raya (Tablero 5x5)
#Aluna: Ortube Rengel Erika Mariana
#Bolivia

#%%
import random
#Tres En Raya (Tablero 3x3)
#Alunos: Caique de Paula Figueiredo Coelho y Lucas Queiroz
#Brasil

#%%
#definicion de funcion que duplicada del tablero de tres en raya y decuelve una copia de este
def getBoardCopy(board):
	duplicateBoard = []

	for i in board:
		duplicateBoard.append(i)

	return duplicateBoard

#definicion de funcion que imprime el tablero de tres en raya (una lista de 25 cadenas que lo representan)
def drawBoard(board):
	#realiza una copia del tablero
	copyBoard = getBoardCopy(board)

	for i in range(1,26):
		if(board[i] == ''):
			copyBoard[i] = str(i)
		else:
			copyBoard[i] = board[i]

	print (' ' + copyBoard[21] + '|' + copyBoard[22] + '|' + copyBoard[23] + '|' + copyBoard[24] + '|' + copyBoard[25])
	print('-----------')

	print (' ' + copyBoard[16] + '|' + copyBoard[17] + '|' + copyBoard[18] + '|' + copyBoard[19] + '|' + copyBoard[20])
	print('-----------')

	print (' ' + copyBoard[11] + '|' + copyBoard[12] + '|' + copyBoard[13] + '|' + copyBoard[14] + '|' + copyBoard[15])
	print('-----------')

	print (' ' + copyBoard[6] + '|' + copyBoard[7] + '|' + copyBoard[8] + '|' + copyBoard[9] + '|' + copyBoard[10])
	print('-----------')

	print (' ' + copyBoard[1] + '|' + copyBoard[2] + '|' + copyBoard[3] + '|' + copyBoard[4] + '|' + copyBoard[5])
	print('-----------')

#%%
#definicion de funcion que elige la letra con la que se quiere jugar 
def inputPlayerLetter():
  	#Devuelve una lista con la letra del humano y la letra de la computadora
	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('Usted quiere ser X u O?')
		letter = input().upper()
		if(letter != 'X' and letter != 'O'):
			print("¡Solo ingresa la letra X si quieres ser X o la letra O si quieres ser O!")

	#El primer elemento de la lista es el jugador humano y el segundo es la computadora.
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

#definicion de funcion que elige al azar quien jugará primero
def whoGoesFirts():
	if random.randint(0, 1) == 0:
		return 'computador'
	else:
		return 'humano'

#%%
#definicion de funcion que hace el movimiento (computador o humano) dependiendo de la letra en el tablero
def makeMove(board, letter, move):
	board[move] = letter

#definicion de funcion que dado un cuadrado y una letra devuelve True si la letra dada gana el juego
def isWinner(board, letter):
	return(
			#-------------------------------DESDE AQUI-----------------------------------
			#fila SUPERIOR 1
            (board[21]==letter and board[22]==letter and board[23]==letter) or # 21 22 23
			(board[22]==letter and board[23]==letter and board[24]==letter) or #22 23 24
			(board[23]==letter and board[24]==letter and board[25]==letter) or #23 24 25

			#fila SUPERIOR 2
            (board[16]==letter and board[17]==letter and board[18]==letter) or #16 17 18
			(board[17]==letter and board[18]==letter and board[19]==letter) or #17 18 19
			(board[18]==letter and board[19]==letter and board[20]==letter) or #18 19 20

			#fila MEDIA
            (board[11]==letter and board[12]==letter and board[13]==letter) or #11 12 13
			(board[12]==letter and board[13]==letter and board[14]==letter) or #12 13 14
			(board[13]==letter and board[14]==letter and board[15]==letter) or #13 14 15

			#fila INFERIOR 2
            (board[6]==letter and board[7]==letter and board[8]==letter) or #6 7 8
			(board[7]==letter and board[8]==letter and board[9]==letter) or #7 8 9
			(board[8]==letter and board[9]==letter and board[10]==letter) or #8 9 10

			#fila INFERIOR 1
            (board[1]==letter and board[2]==letter and board[3]==letter) or #1 2 3
			(board[2]==letter and board[3]==letter and board[4]==letter) or #2 3 4
			(board[3]==letter and board[4]==letter and board[5]==letter) or #3 4 5

			#columna IZQUIERDA 1
            (board[21]==letter and board[16]==letter and board[11]==letter) or #21 16 11
			(board[16]==letter and board[11]==letter and board[6]==letter) or #16 11 6
			(board[11]==letter and board[6]==letter and board[1]==letter) or #11 6 1

			#columna IZQUIERDA 2
            (board[22]==letter and board[17]==letter and board[12]==letter) or #22 17 12
			(board[17]==letter and board[12]==letter and board[7]==letter) or #17 12 7
			(board[12]==letter and board[7]==letter and board[2]==letter) or #12 7 2

			#columna MEDIA
            (board[23]==letter and board[18]==letter and board[13]==letter) or #23 18 13
			(board[18]==letter and board[13]==letter and board[8]==letter) or #18 13 8
			(board[13]==letter and board[8]==letter and board[3]==letter) or #13 8 3

			#columna DERECHA 2
            (board[24]==letter and board[19]==letter and board[14]==letter) or #24 29 14
			(board[19]==letter and board[14]==letter and board[4]==letter) or #19 14 9
			(board[14]==letter and board[9]==letter and board[4]==letter) or #14 9 4

			#columna DERECHA 1
            (board[25]==letter and board[20]==letter and board[15]==letter) or #25 20 15
			(board[20]==letter and board[15]==letter and board[10]==letter) or #20 15 10
			(board[15]==letter and board[10]==letter and board[5]==letter) or #15 10 5
			#-------------------HASTA AQUI SON 30 POSIBLES SOLUCIONES--------------------

			#-------------------------------DESDE AQUI-----------------------------------
			#diagonal 5 (inicia cuadro 23)
            (board[23]==letter and board[19]==letter and board[15]==letter) or #23 19 15

			#diagonal 4 (inicia cuadro 22)
            (board[22]==letter and board[18]==letter and board[14]==letter) or #22 18 14
			(board[18]==letter and board[14]==letter and board[10]==letter) or #18 14 10

			#diagonal 3 (inicia cuadro 21)
            (board[21]==letter and board[17]==letter and board[13]==letter) or #21 17 13
			(board[17]==letter and board[13]==letter and board[9]==letter) or #17 13 9
			(board[13]==letter and board[9]==letter and board[5]==letter) or #13 9 5

			#diagonal 2 (inicia cuadro 16)
            (board[16]==letter and board[12]==letter and board[8]==letter) or #16 12 8
			(board[12]==letter and board[8]==letter and board[4]==letter) or #12 8 4

			#diagonal 1 (inicia cuadro 11)
            (board[11]==letter and board[7]==letter and board[3]==letter) or #11 7 3
			#-------------------HASTA AQUI SON 9 POSIBLES SOLUCIONES--------------------

			#-------------------------------DESDE AQUI-----------------------------------
			#diagonal 5 (inicia cuadro 23)
            (board[23]==letter and board[17]==letter and board[11]==letter) or #23 17 11

			#diagonal 4 (inicia cuadro 22)
            (board[24]==letter and board[18]==letter and board[12]==letter) or #24 18 12
			(board[18]==letter and board[12]==letter and board[6]==letter) or #18 12 6
			
			#diagonal 3 (inicia cuadro 25)
            (board[25]==letter and board[19]==letter and board[13]==letter) or #25 19 13
			(board[19]==letter and board[13]==letter and board[7]==letter) or #19 13 7
			(board[13]==letter and board[19]==letter and board[13]==letter) or #13 7 1

			#diagonal 2 (inicia cuadro 20)
            (board[20]==letter and board[14]==letter and board[8]==letter) or #20 14 8
			(board[14]==letter and board[8]==letter and board[2]==letter) or #14 8 2

			#diagonal 1 (inicia cuadro 11)
            (board[15]==letter and board[9]==letter and board[3]==letter)#15 9 3
			#-------------------HASTA AQUI SON 9 POSIBLES SOLUCIONES--------------------

			#EN TOTAL SON 48 SOLUCIONES POSIBLES
        ) 

#%%
#deficnion de funcion que devuelve verdadero si el espacio solicitado está libre en el tablero
def isSpaceFree(board, move):
	if(board[move] == ''):
		return True
	else:
		return False

#definicion de funcion que obtiene el movimiento de quien está jugando (computadora o humano)
def getPlayerMove(board):
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split() or not isSpaceFree(board, int(move)):
		print('Cual es su proximo movimiento?')
		move = input()

		#si el movimiento no está entre 1 y 25 devulve juaga invlaida
		if(move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'):
			print("MOVIMENTO INVALIDO!")
		
		#si el movimiento está entre 1 y 25 pero el cuadrado escogido ya está ocupado devuelve espacio no disponible
		if(move in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'):
			if(not isSpaceFree(board, int(move))):
				print("ESPACIO NO DISPONIBLE! ELIJA OTRO ESPACO DISPONIBLE EN EL TABLERO!")

	return int(move)

#%%
#definicion de funcion que devuelbe un movimiento random valido, devuelve None si no hay movimientos válidos
def chooseRandomMoveFromList(board, movesList):
	possiveisMovimentos = []
	for i in movesList:
		if isSpaceFree(board, i):
			possiveisMovimentos.append(i)

	if len(possiveisMovimentos) != 0:
		return random.choice(possiveisMovimentos)
	else:
		return None

##definicion de funcion que devuelve True si todos los espacios del tablero están disponibles
def isBoardFull(board):
	for i in range(1, 26):
		if isSpaceFree(board, i):
			return False
	return True

#definicion de funcion que devulve la lista de todos los espacios que están disponibles en el tablero
def possiveisOpcoes(board):
	opcoes = []

	for i in range(1, 26):
		if isSpaceFree(board, i):
			opcoes.append(i)

	return opcoes

#%%
#definicion de funcion que comprueba si el juego ha llegado al final
def finishGame(board, computerLetter):
	#Retorna -1 si el humano gana
	#Retorna 1 si la computadora gana
	#Retorna 0 si el juego termina en empate
	#Retorna None si el juego no ha terminado

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	#si la letra de la computadora ganó deuelve 1 
	if(isWinner(board, computerLetter)):
		return 1

	elif(isWinner(board, playerLetter)):
		return -1

	elif(isBoardFull(board)):
		return 0

	else:
		return None

#%%
#definicion de funcion para poda alphaBeta
def alphabeta(board, computerLetter, turn, alpha, beta):

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if turn == computerLetter:
		nextTurn = playerLetter
	else:
		nextTurn = computerLetter

	finish = finishGame(board, computerLetter)

	if (finish != None):
		return finish

	possiveis = possiveisOpcoes(board)

	#alpha = el valor de la mejor acción que se ha encontrado en cualquier punto de la búsqueda para Max (computador)
	#beta = el valor de la mejor acción que se ha encontrado en cualquier punto de la búsqueda para Min (humano)
	#val = valor
	#si es el turno del computador 
	if turn == computerLetter:
		#para un movimiento en los posibles movimientos que hay
		for move in possiveis:
			#hace un movimiento
			makeMove(board, turn, move)
			#valor tomaria el valor de la funcion alphaBeta tomando en cuenta el tablero, la letra de la computadora, el siguiente turno,
			#alpha (computador) y beta (humano)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			#y hace el movimiento tomando en cuenta lo anterior
			makeMove(board, '', move)
			#si el valor de hacer un movimiento es mayor al valor del movimiento que hace el computador
			#entonces alpha toma el valor de val, porque lo que busca es econtrar el valor mas grande para el computador
			if val > alpha:
				alpha = val

			if alpha >= beta:
				return alpha
		return alpha

	else:
		#para un movimiento en los posibles movimientos que hay
		for move in possiveis:
			#hace un movimiento
			makeMove(board, turn, move)
			#valor tomaria el valor de la funcion alphaBeta tomando en cuenta el tablero, la letra de la computadora, el siguiente turno,
			#alpha (computador) y beta (humano)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			#y hace el movimiento tomando en cuenta lo anterior
			makeMove(board, '', move)
			#si el valor de hacer un movimiento es mayor al valor del movimiento del humano,
			#entonces devulve beta, porque lo que se busca es encontrar el valor más pequeño para el humano
			if  val > beta:
				return beta

			if alpha <= beta:
				return beta
		return beta

#%%
#definicion de funcion que define cual sera el movimiento de la computadora
def getComputerMove(board, turn, computerLetter):
	a = -2
	opcoes = []

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	#Iniciamos aqui con el MiniMax
	#Primero verificamos si podemos ganar en el siguiente movimiento
	for i in range(1, 26):
		copy = getBoardCopy(board)
		#si el espacio no está ocupado
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			#si el ganador es la letra del computador
			if isWinner(copy, computerLetter):
				return i

	#Comprueba si el humano puede ganar en el siguiente movimiento y lo bloquea
	for i in range(1, 26):
		copy = getBoardCopy(board)
		#si el espacio no está ocupado
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			#si el ganador es la letra del humano
			if isWinner(copy, playerLetter):
				return i

	possiveisOpcoesOn = possiveisOpcoes(board)

	for move in possiveisOpcoesOn:
		makeMove(board, computerLetter, move)
		val = alphabeta(board, computerLetter, playerLetter, -2, 2)		
		makeMove(board, '', move)

		if val > a:
			a = val
			opcoes = [move]

		elif val == a:
			opcoes.append(move)

	return random.choice(opcoes)

print('¡Juguemos al tres en raya!')

jogar = True

while jogar:
	#Reinicia el juego
	theBoard = [''] * 26
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirts()
	print('O ' + turn +' juega primero')
	gameisPlaying = True

	while gameisPlaying:
		if turn == 'humano':
			#Turno del humano
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('Woooow! ¡Ganaste el juego!')
				gameisPlaying = False
			
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('El juego terminó en empate')
					break
				else:
					turn = 'computador'

		else:
			#Turno de la computadora
			move = getComputerMove(theBoard, playerLetter, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print("La computadora ganó   :'(")
				gameisPlaying = False

			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('El juego terminó en empate')
					break
				else:
					turn = 'humano'

	letterNew = ''
	while not(letterNew == 'S' or letterNew == 'N'):
		print("Quiere jugar otra vez? S(para SI) o N(para NO)")
		letterNew = input().upper()
		if (letterNew != 'S' and letterNew != 'N'):
			print("Entrada invalida! Digite S(para SI) o N(para NO)")
		if(letterNew == 'N'):
			print("¡Fue bueno jugar contigo! ¡Hasta luego!")
			jogar = False