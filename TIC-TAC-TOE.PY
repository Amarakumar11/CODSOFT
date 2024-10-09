import math

# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]  # Empty board represented as a list

# Display the board in a 3x3 grid format
def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Check if there is a winner
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Check if the board is full (draw)
def check_draw(board):
    return ' ' not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1  # AI wins
    elif check_winner(board, 'X'):
        return -1  # Human wins
    elif check_draw(board):
        return 0  # Draw

    if is_maximizing:  # AI's turn (O)
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:  # Human's turn (X)
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

# Find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # AI plays as 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Handle human player's move
def player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'  # Human plays as 'X'
                break
            else:
                print("That spot is already taken.")
        else:
            print("Invalid input. Please choose a number between 1 and 9.")

# Main game loop
def play_game():
    board = initialize_board()
    display_board(board)

    while True:
        # Human move
        player_move(board)
        display_board(board)
        if check_winner(board, 'X'):
            print("You win! Congratulations!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making its move...")
        ai_move = best_move(board)
        board[ai_move] = 'O'
        display_board(board)
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()