
from player import HumanPlayer, RandomComputer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_move(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']
        # return[]
        moves = []
        # for (i, spot) in enumerate(self.board):
        #    ['x', 'x', 'x'] --> [(0, 'x'), (1, 'x'), (2, 'o')
        #    if spot == ' ':
        #       moves.append(i)
        # return moves

    def empty_squares(self):
        return '' in self.board

    def num_empty_squares(self):
        return len(self.available_move())

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all[(spot == letter for spot in row)]:
            return True
        col_ind = square % 3
        colum = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in colum]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all ([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game = True ):
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about the winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        if leter == 'o':
            square = o_player.get.move(game)
        else:
            square = x_player.get.move(game)
        # let's define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f'make a move to square {square}')
                game.print_board()
                print('') # just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = '0' if letter == 'X' else 'X'
            # if letter == 'X':
            #    letter = 'O'
            # else:
            letter = 'X'
        if print_game:
            print('It\s a tie')
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputer
    t = TicTacToe
    play(t, x_player, o_player, print_game=True)
