#!/usr/bin/python3

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Runs the Tic-Tac-Toe game."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    max_moves = 9

    while not check_winner(board) and moves < max_moves:
        print_board(board)

        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2 for both row and column.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                moves += 1
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            print("Invalid input. Please enter numeric values only.")

    print_board(board)

    if check_winner(board):
        # Switch back to the winning player
        winner = "O" if player == "X" else "X"
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
