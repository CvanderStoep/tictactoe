import random

def AI_move(board):
    all_moves = board.legal_moves()
    random_move = random.choice(all_moves)
    return random_move
