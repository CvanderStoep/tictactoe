from board import Board
from random_move import AI_move
board = Board()


def play_move():
    # X = human player
    if board.current_player == 'X':
        print('next move for X')
        print(board.legal_moves())
        valid_move = False
        while not valid_move:
            move = int(input('give next move(0-8): '))
            if move in board.legal_moves():
                valid_move = True
            else:
                print('invalid move')
                print(board.legal_moves())
        board.board[move] = board.current_player
    # O = computer player
    else:
        # print('next move for O:')
        move = AI_move(board)
        print('Move for O: ' + str(move))
        board.board[move] = board.current_player
    return


# main program loop
while not board.game_has_ended:
    board.print_board()
    play_move()
    board.check_winner()
    if not board.game_has_ended:
        board.check_draw()
    else:
        board.print_board()
    board.change_player()


print('game ended.')
input('key stroke')
