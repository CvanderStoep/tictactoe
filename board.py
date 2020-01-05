class Board:
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    game_has_ended = False
    current_player = 'X'

    winning_lines = [(0,1,2),(3,4,5),(6,7,8),
                     (0,3,6),(1,4,7),(2,5,8),
                     (0,4,8),(2,4,6)]

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

    def check_winner(self):
        winner = None
        for (x,y,z) in self.winning_lines:
            if self.board[x] == self.board[y] == self.board[z]:
                winner = self.board[x]
                self.game_has_ended = True
                break

        if self.game_has_ended:
            self.print_board()
            print('Winner is: ', winner)

        return

    def change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        return

    def legal_moves(self):
        list_of_legal_moves = []
        for i in range(0,9):
            if self.board[i] ==i:
                list_of_legal_moves.append(i)
        return list_of_legal_moves

