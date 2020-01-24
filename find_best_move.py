def find_best_move(board):
    # finds the best move for O (opponent; computer)
    best_value = +1000
    best_move = -1
    for move in board.legal_moves():
        board.board[move] = board.current_player
        depth = 0
        maximizing_player = True
        current_score = mini_max(board, depth, maximizing_player)  # O has made the move, now evaluate X
        if current_score is not None and current_score < best_value:
            best_move = move
            best_value = current_score
        board.board[move] = move  # undo the move
    return best_move


def mini_max(board, depth, isMaximizingPlayer):
    current_score = board.return_score()
    if current_score is not None:  # this means the game is ended (win/lose/draw)
        if current_score == 10:
            current_score -= depth
        elif current_score == -10:
            current_score += depth
        return current_score
    if isMaximizingPlayer:
        best_value = -1000
        current_player = 'X'
        for move in board.legal_moves():
            board.board[move] = current_player
            best_value = max(best_value, mini_max(board, depth + 1, not isMaximizingPlayer))
            board.board[move] = move  # undo the move
        return best_value
    else:
        best_value = 1000
        current_player = 'O'
        for move in board.legal_moves():
            board.board[move] = current_player
            best_value = min(best_value, mini_max(board, depth + 1, not isMaximizingPlayer))
            board.board[move] = move  # undo the move
        return best_value




