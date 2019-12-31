from board import Board

board = Board()

def play_move():
    if board.current_player == 'X':
        print('next move for X')
    else:
        print('next move for O:')

    move = int(input('give next move(0-8): '))
    board.board[move] = board.current_player
    return


# main program loop
while not board.game_has_ended:
    board.print_board()
    play_move()
    board.change_player()
    board.check_draw()
    if (not board.game_has_ended):
        board.check_winner()
    else:
        board.print_board()

print('game ended.')
input('key stroke')
