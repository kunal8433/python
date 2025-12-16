# Tic Tac Toe Game in Python (Console Version)
# Beginner friendly – run this file in VS Code

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print("\n")
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print("\n")

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check draw
def check_draw():
    return ' ' not in board

# Main game loop
def play_game():
    current_player = 'X'

    while True:
        print_board()
        print(f"Player {current_player} turn")
        
        try:
            move = int(input("Enter position (1-9): ")) - 1
        except ValueError:
            print("Please enter a number between 1 to 9")
            continue

        if move < 0 or move > 8:
            print("Invalid position! Choose 1 to 9")
            continue

        if board[move] != ' ':
            print("Position already taken!")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins! 🎉")
            break

        if check_draw():
            print_board()
            print("Game Draw!")
            break

        # Switch player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

# Start the game
print("Welcome to Tic Tac Toe")
print("Positions are like this:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

play_game()
