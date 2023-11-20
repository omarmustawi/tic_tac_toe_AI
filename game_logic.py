# Check for a winner
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False
#  ========================== THE END ==============================



# Check for a tie
def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)
#  ========================== THE END ==============================
