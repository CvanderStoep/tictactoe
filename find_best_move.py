def find_best_move(board):
    best_value = +1000
    best_move = -1
    for move in board.legal_moves():
        board.board[move] = board.current_player
        # current_score = board.return_score()
        current_score = mini_max(board, 0, True)  # O has made the move, now evaluate X
        if current_score is not None and current_score < best_value:
            best_move = move
            best_value = current_score
        board.board[move] = move  # undo the move
    return best_move


def mini_max(board, depth, isMax):
    current_score = board.return_score()
    if current_score is not None:  # this means the game is ended (win/lose/draw)
        return current_score
    if isMax:
        best_value = -1000
        current_player = 'X'
        for move in board.legal_moves():
            board.board[move] = current_player
            best_value = max(best_value, mini_max(board, depth+1, not isMax))
            board.board[move] = move  # undo the move
        return best_value
    else:
        best_value = 1000
        current_player = 'O'
        for move in board.legal_moves():
            board.board[move] = current_player
            best_value = min(best_value, mini_max(board, depth+1, not isMax))
            board.board[move] = move  # undo the move
        return best_value




