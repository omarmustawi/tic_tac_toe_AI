from game_logic import check_tie, check_winner


def minimax(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'tie': 0}

    winner = check_winner(board, 'X')
    if winner:
        return scores['X']

    winner = check_winner(board, 'O')
    if winner:
        return scores['O']

    if check_tie(board):
        return scores['tie']

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '  # undo the move
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '  # undo the move
                    min_eval = min(min_eval, eval)
        return min_eval
