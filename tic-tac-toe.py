# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Función para verificar si hay un ganador
def check_winner(board, player):
    # Comprobar filas, columnas y diagonales
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Función para verificar si el tablero está lleno
def is_board_full(board):
    return all([spot != " " for row in board for spot in row])

# Función principal del juego
def play_game():
    # Inicializar el tablero
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    # Bucle del juego
    while True:
        print_board(board)
        print(f"Turno de {current_player}:")
        
        # Pedir posición
        row = int(input("Selecciona fila (0, 1, 2): "))
        col = int(input("Selecciona columna (0, 1, 2): "))
        
        # Validar si la casilla está libre
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Esa casilla ya está ocupada. Intenta otra vez.")
            continue
        
        # Verificar si hay un ganador
        if check_winner(board, current_player):
            print_board(board)
            print(f"¡El jugador {current_player} ha ganado!")
            break
        
        # Verificar si hay empate
        if is_board_full(board):
            print_board(board)
            print("¡Empate!")
            break
        
        # Cambiar de jugador
        current_player = "O" if current_player == "X" else "X"

# Iniciar el juego
play_game()
