import math

# Define the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Define the initial board
def create_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Check for winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    # Check for tie
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return None
    return 'Tie'

# Check if moves are left
def is_moves_left(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return True
    return False

# Minimax algorithm
def minimax(board, depth, is_max):
    score = check_winner(board)
    
    if score == PLAYER_X:
        return -10 + depth
    if score == PLAYER_O:
        return 10 - depth
    if score == 'Tie':
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = EMPTY
        return best

# Find the best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Main game loop
def play_game():
    board = create_board()
    current_player = PLAYER_X

    while True:
        print_board(board)
        if check_winner(board) or not is_moves_left(board):
            break

        if current_player == PLAYER_X:
            row, col = map(int, input("Enter row and column (0-2) for X: ").split())
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                current_player = PLAYER_O
        else:
            print("AI is making a move...")
            row, col = find_best_move(board)
            board[row][col] = PLAYER_O
            current_player = PLAYER_X

    winner = check_winner(board)
    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"The winner is {winner}!")

# Start the game
play_game()
