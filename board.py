class Board:
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    current_player = 'X'

    winning_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6)]

    def print_board(self):
        print(self.board[0], '|', self.board[1], '|', self.board[2])
        print(self.board[3], '|', self.board[4], '|', self.board[5])
        print(self.board[6], '|', self.board[7], '|', self.board[8])
        return

    def check_draw(self):
        game_draw = True
        for i in range(0, 9):
            if self.board[i] == i:
                game_draw = False
        return game_draw

    def check_winner(self):
        # returns the winner (X or O) or None otherwise
        winner = None
        for (x, y, z) in self.winning_lines:
            if self.board[x] == self.board[y] == self.board[z]:
                winner = self.board[x]
                break
        return winner

    def game_has_ended(self):
        # returns True if there is a winner OR there is a draw
        winner = self.check_winner()
        if winner is not None:
            return True
        return self.check_draw()
        pass

    def change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        return

    def legal_moves(self):
        list_of_legal_moves = []
        for i in range(0, 9):
            if self.board[i] == i:
                list_of_legal_moves.append(i)
        return list_of_legal_moves

    def return_score(self):
        #returns the score of the current state
        #10 if X has won
        #-10 if O has won
        #0 if there is a draw
        #None otherwise
        score = None
        winner = self.check_winner()
        if winner is not None:
            if winner == 'X':
                score = 10
            elif winner == 'O':
                score = -10
        if self.check_draw():
            score = 0
        return score
