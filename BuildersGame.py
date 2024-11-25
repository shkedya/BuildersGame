# Author: Alon Shkedy
# Description: Returns a set of the common words in two strings

class BuildersGame:
    """
    Represents the board for a two-player game that is played on a 5x5 grid
    """

    def __init__(self):
        """Initializes the values of the class"""
        self._current_state = ["X_WON", "O_WON", "UNFINISHED"]
        self._gamestate = 2
        self._game_started = False
        self._player1_turn = True
        self._board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self._player1 = [[[0 for column in range(5)] for row in range(5)] for height in range(3)]
        self._player2 = [[[0 for column in range(5)] for row in range(5)] for height in range(3)]

    def get_current_state(self):
        """Returns the current state"""
        return self._current_state[self._gamestate]

#    def print_board(self, theboard):
#        for row in range(5):
#            print(theboard[row])
#        print("")

    def initial_placement(self, first_row, first_column, second_row, second_column, which_player):
        """Player x or Player o places their first two pieces on the 5x5 grid"""
        allowed_numbers = {0, 1, 2, 3, 4}
        if which_player == "x" and not self._player1_turn:
            return False
        if which_player == "o" and self._player1_turn:
            return False
        if first_row not in allowed_numbers or first_column not in allowed_numbers or second_row not in allowed_numbers\
                or second_column not in allowed_numbers:
            return False
        if second_row == first_row and first_column == second_column:
            return False
        if self._board[first_row][first_column] > 0:
            return False
        if self._board[second_row][second_column] > 0:
            return False
        self._board[first_row][first_column] = 1
        self._board[second_row][second_column] = 1
        if self._player1_turn:
            self._player1[0][first_row][first_column] = 1
            self._player1[0][second_row][second_column] = 1
            self._player1_turn = False
        else:
            self._player2[0][first_row][first_column] = 1
            self._player2[0][second_row][second_column] = 1
            self._game_started = True
            self._player1_turn = True
        return True
 #       self.print_board(self._board)

    def valid_move(self, row_start, column_start, row_end, column_end, row_build, column_build):
        """Checking if a move is valid"""
        allowed_numbers = {0, 1, 2, 3, 4}
        if row_start not in allowed_numbers or column_start not in allowed_numbers or row_end not in allowed_numbers \
                or column_end not in allowed_numbers or row_build not in allowed_numbers \
                or column_build not in allowed_numbers:
            return False
        if self._game_started is False:
            return False
        if abs(row_end - row_start) > 1:
            return False
        if abs(column_end - column_start) > 1:
            return False
        if abs(row_end - row_build) > 1:
            return False
        if abs(column_end - column_build) > 1:
            return False
        if self._gamestate != 2:
            return False
        current_height = self._board[row_start][column_start] - 1
        if current_height < 0:
            return False
        if self._player1_turn is True and self._player1[current_height][row_start][column_start] == 0:
            return False
        if self._player1_turn is False and self._player2[current_height][row_start][column_start] == 0:
            return False
        if self._board[row_build][column_build] > 0:
            return False
        target_height = self._board[row_end][column_end] - 1
        if target_height - current_height > 1:
            return False
        return True

    def make_move(self, row_start, column_start, row_end, column_end, row_build, column_build):
        """Move a builder from a given state and then place another builder"""
        check_move = self.valid_move(row_start, column_start, row_end, column_end, row_build, column_build)
        if check_move is False:
            return False
        current_height = self._board[row_start][column_start] - 1
        target_height = self._board[row_end][column_end]
        self._board[row_end][column_end] += 1
        self._board[row_start][column_start] -= 1
        self._board[row_build][column_build] = 1
        if self._player1_turn is True:
            if self._board[row_end][column_end] == 4:
                self._gamestate = 0
                return True
            self._player1[target_height][row_end][column_end] = 1
            self._player1[current_height][row_start][column_start] = 0
            self._player1[0][row_build][column_build] = 1
            self._player1_turn = False
            for row in range(5):
                for column in range(5):
                    for move_row in range(-1, 2):
                        for move_column in range(-1, 2):
                            for build_row in range(-1, 2):
                                for build_column in range(-1, 2):
                                    check_move = self.valid_move(row, column, row+move_row, column+move_column,
                                                                 row+build_row, column+build_column)
                                    if check_move is True:
                                        return True
            self._gamestate = 0
            return True
        else:
            if self._board[row_end][column_end] == 4:
                self._gamestate = 1
                return True
#            print(target_height, current_height)
            self._player2[target_height][row_end][column_end] = 1
            self._player2[current_height][row_start][column_start] = 0
            self._player2[0][row_build][column_build] = 1
            self._player1_turn = True
            for row in range(5):
                for column in range(5):
                    for move_row in range(-1, 2):
                        for move_column in range(-1, 2):
                            for build_row in range(-1, 2):
                                for build_column in range(-1, 2):
                                    check_move = self.valid_move(row, column, row + move_row, column + move_column,
                                                                 row + build_row, column + build_column)
                                    if check_move is True:
                                        return True
            self._gamestate = 1
            return True

#        self.print_board(self._board)
#        print("player1")
#        self.print_board(self._player1[0])
#        print("player2")
#        self.print_board(self._player2[0])
#        print("player2level2")
#        self.print_board(self._player2[1])


# game = BuildersGame()
# game.initial_placement(2,2,1,2,'x')
# game.initial_placement(0,1,4,2,'o')
# game.make_move(2,2,1,1,1,0)
# game.make_move(0,1,1,0,2,0)
# print(game.get_current_state())
