def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    moves = 0

    while moves < 9:
        print_board(board)
        player = players[moves % 2]
        print(f"Player {player}'s turn")

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] == " ":
            board[row][col] = player
            moves += 1
        else:
            print("Cell already taken, try again!")
            continue

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

    print_board(board)
    print("It's a draw!")

# Run the game
tic_tac_toe()
