board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
game_has_ended = False
current_player = 'X'
game_draw = False
winner = None


def print_board():
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])
    return



def play_move():
    global current_player
    if current_player == 'X':
        print('next move for X')
    else:
        print('next move for O:')

    move = int(input('give next move(0-8): '))
    board[move] = current_player
    return


def check_draw():
    global game_draw, game_has_ended
    game_has_ended = True
    game_draw = True
    for i in range(0, 9):
        if board[i] == i:
            game_draw = False
            game_has_ended = False
    if game_draw:
        print_board()
        print('game has ended in a draw!')
    return


def check_winner():
    global winner, game_has_ended
    winner, game_has_ended = check_column()
    if game_has_ended:
        print_board()
        print('winner is: ', winner)
        return

    winner, game_has_ended = check_row()
    if game_has_ended:
        print_board()
        print('winner is: ', winner)
        return

    winner, game_has_ended = check_diagonal()
    if game_has_ended:
        print_board()
        print('winner is: ', winner)
    return


def check_column():
    if board[0] == board[3] == board[6]:
        winner = board[0]
        game_has_ended = True
    elif board[1] == board[4] == board[7]:
        winner = board[1]
        game_has_ended = True
    elif board[2] == board[5] == board[8]:
        winner = board[2]
        game_has_ended = True
    else:
        winner = None
        game_has_ended = False
    return (winner, game_has_ended)


def check_row():
    # global winner, game_has_ended
    if board[0] == board[1] == board[2]:
        winner = board[0]
        game_has_ended = True
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        game_has_ended = True
    elif board[6] == board[7] == board[8]:
        winner = board[6]
        game_has_ended = True
    else:
        winner = None
        game_has_ended = False
    return (winner, game_has_ended)


def check_diagonal():
    # global winner, game_has_ended
    if board[0] == board[4] == board[8]:
        winner = board[4]
        game_has_ended = True
    elif board[2] == board[4] == board[6]:
        winner = board[4]
        game_has_ended = True
    else:
        winner = None
        game_has_ended = False
    return (winner, game_has_ended)


def change_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    return


# main program loop
while not game_has_ended:
    print_board()
    play_move()
    change_player()
    check_draw()
    check_winner()

print('game ended.')
input('key stroke')
