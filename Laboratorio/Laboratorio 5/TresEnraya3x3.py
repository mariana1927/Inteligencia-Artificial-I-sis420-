#%%
import random

#%%
def getBoardCopy(board):
	#realiza un duplicado del tablero del tres en raya y decuelve una copia de este
	duplicateBoard = []

	for i in board:
		duplicateBoard.append(i)

	return duplicateBoard

#definicion de funcion que imprime el tablero del tres en raya, que es una list de 9 cadenas que lo representan
def drawBoard(board):
	copyBoard = getBoardCopy(board)

	for i in range(1,10):
		if(board[i] == ''):
			copyBoard[i] = str(i)
		else:
			copyBoard[i] = board[i]
	print('' + copyBoard[7] + '|' + copyBoard[8] + '|' + copyBoard[9])
	print('-------')

	print('' + copyBoard[4] + '|' + copyBoard[5] + '|' + copyBoard[6])
	print('-------')

	print('' + copyBoard[1] + '|' + copyBoard[2] + '|' + copyBoard[3])
	print('-------')

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

def whoGoesFirts():
	#Elige al azar al jugador que jugará primero
	if random.randint(0, 1) == 0:
		return 'computador'
	else:
		return 'humano'

#%%
def makeMove(board, letter, move):
	#Hace el movimiento de la computadora o del jugador dependiendo de la letra en el tablero
	board[move] = letter

def isWinner(board, letter):
	#Dado un cuadrado y una letra, esta función devuelve True si la letra dada gana el juego.
	return(
           	(board[7] == letter and board[8] == letter and board[9] == letter) or #linea superior
            (board[4] == letter and board[5] == letter and board[6] == letter) or #linea del medio
            (board[1] == letter and board[2] == letter and board[3] == letter) or #linea de abajo
            (board[7] == letter and board[4] == letter and board[1] == letter) or #columna de la izquierda
            (board[8] == letter and board[5] == letter and board[2] == letter) or #columna del medio
			(board[9] == letter and board[6] == letter and board[3] == letter) or #columna da la derecha
            (board[7] == letter and board[5] == letter and board[3] == letter) or #diagonal principal
            (board[9] == letter and board[5] == letter and board[1] == letter) #diagonal secundaria
        )

#%%
def isSpaceFree(board, move):
	#Devuelve True si el espacio solicitado está libre en el tablero
	if(board[move] == ''):
		return True
	else:
		return False

def getPlayerMove(board, lugar_no_disponible):
	#Recibe el movimiento del jugador
	move = ''
	
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('Cual es su proximo movimiento? (1-9)')
		move = input()
		if(move not in '1 2 3 4 5 6 7 8 9'):
			print("MOVIMENTO INVALIDO!")
		
		if lugar_no_disponible <= 6 and move =='5':
			print('lugar no disponible')

		if(move in '1 2 3 4 5 6 7 8 9'):
			print('move: ', move)
			if(not isSpaceFree(board, int(move))):
				print("ESPACIO NO DISPONIBLE! ELIJA CUALQUIER NUMERO DISPONIBLE EN EL TABLERO!")

	return int(move)

#%%
#definicion de funcion que devuelbe un movimiento random valido, devuelve None si no hay movimientos válidos
def chooseRandomMoveFromList(board, movesList, nrot):
	possiveisMovimentos = []
	for i in movesList:
		if isSpaceFree(board, i):
			possiveisMovimentos.append(i)

	if len(possiveisMovimentos) != 0:
		return random.choice(possiveisMovimentos)
	else:
		return None

#definicion de funcion que devuelve True si todos los espacios del tablero están disponibles
def isBoardFull(board):
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False
	return True

#definicion de funcion que devulve la lista de todos los espacios que están disponibles en el tablero
def possiveisOpcoes(board):
	opcoes = []

	for i in range(1, 10):
		if isSpaceFree(board, i):
			opcoes.append(i)

	return opcoes

#%%
theBoard = [''] * 10

makeMove(theBoard, 'X', 8)
makeMove(theBoard, 'O', 3)

#drawBoard(theBoard)

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

	if turn == computerLetter:
		for move in possiveis:
			makeMove(board, turn, move)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			makeMove(board, '', move)
			if val < alpha:
				alpha = val

			if alpha <= beta:
				return alpha
		return alpha

	else:
		for move in possiveis:
			makeMove(board, turn, move)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			makeMove(board, '', move)
			if val < beta:
				beta = val

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
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i

	#Comprueba si el humano puede ganar en el siguiente movimiento y lo bloquea
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
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
	theBoard = [''] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirts()
	print('O ' + turn +' juega primero,')
	gameisPlaying = True

	while gameisPlaying:
		if turn == 'humano':
			#Turno del humano
			drawBoard(theBoard)
			move = getPlayerMove(theBoard, lugar_no_disponible = 5)
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
				print("La computadora ganó :(")
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
			print("Entrada invalida! Digite S(para SI) o N(para NO)!")
		if(letterNew == 'N'):
			print("¡Fue bueno jugar contigo! ¡Hasta luego!")
			jogar = False