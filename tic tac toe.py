def the_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n---------")

def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def Winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def play_tic_tac_toe():
    print("you are playing tic tac toe")
    board = the_board()
    current_player = "X"

    while True:
        print_board(board)

        row = int(input("Enter the row (0-2): "))

        column = int(input("Enter the column (0-2): "))

        if board[row][column] == " ":
            board[row][column] = current_player
        else:
            print("not valid")
            continue

        if Winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif board_full(board):
            print_board(board)
            print("thats a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

play_tic_tac_toe()