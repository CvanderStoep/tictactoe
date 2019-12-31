class Board:
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    game_has_ended = False
    current_player = 'X'

    def print_board(self):
        print(self.board[0], '|', self.board[1], '|', self.board[2])
        print(self.board[3], '|', self.board[4], '|', self.board[5])
        print(self.board[6], '|', self.board[7], '|', self.board[8])
        return

    def check_draw(self):
        self.game_has_ended = True
        game_draw = True
        for i in range(0, 9):
            if self.board[i] == i:
                game_draw = False
                self.game_has_ended = False
        if game_draw:
            self.print_board()
            print('game has ended in a draw!')
        return

    def check_column(self):
        if self.board[0] == self.board[3] == self.board[6]:
            winner = self.board[0]
            self.game_has_ended = True
        elif self.board[1] == self.board[4] == self.board[7]:
            winner = self.board[1]
            self.game_has_ended = True
        elif self.board[2] == self.board[5] == self.board[8]:
            winner = self.board[2]
            self.game_has_ended = True
        else:
            winner = None
        return winner

    def check_row(self):
        if self.board[0] == self.board[1] == self.board[2]:
            winner = self.board[0]
            self.game_has_ended = True
        elif self.board[3] == self.board[4] == self.board[5]:
            winner = self.board[3]
            self.game_has_ended = True
        elif self.board[6] == self.board[7] == self.board[8]:
            winner = self.board[6]
            self.game_has_ended = True
        else:
            winner = None
        return winner

    def check_diagonal(self):
        if self.board[0] == self.board[4] == self.board[8]:
            winner = self.board[4]
            self.game_has_ended = True
        elif self.board[2] == self.board[4] == self.board[6]:
            winner = self.board[4]
            self.game_has_ended = True
        else:
            winner = None
        return winner

    def check_winner(self):
        winner = self.check_column()
        if self.game_has_ended:
            self.print_board()
            print('winner is: ', winner)
            return

        winner = self.check_row()
        if self.game_has_ended:
            self.print_board()
            print('winner is: ', winner)
            return

        winner = self.check_diagonal()
        if self.game_has_ended:
            self.print_board()
            print('winner is: ', winner)
            return

        return

    def change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        return
