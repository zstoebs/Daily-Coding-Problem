"""
@author Zach Stoebner
@date 12-16-2019
@descrip Connect 4 is a game where opponents take turns dropping red or black discs into a
7 x 6 vertically suspended grid. The game ends either when one player creates a line of
four consecutive discs of their color (horizontally, vertically, or diagonally), or when
there are no more spots left in the grid.

Design and implement Connect 4.
"""

from abc import ABC

class Grid(ABC):

    def __init__(self):

        # in this grid each row is an actual col in the game and each col is really a row
        # since each falls to the end of the column it will be more direct to manage the columns this way
        self.grid = [[""]*7 for _ in range(6)]
        self.valids = list(range(6))

    def add_piece(self,color="",col=-1):
        if col in self.valids:
            empty = True
            i = 0
            for row in self.grid[col]:
                if row != "":
                    self.grid[col][i-1] = color
                    empty = False

                    # if filling in last spot on col, remove from valid cols
                    if i == 1:
                        self.valids.remove(col)
                    break
                i += 1
            if empty:
                self.grid[col][-1] = color
            return True
        return False

    def check_win_scenario(self):
        pass

class Connect4_Game(Grid):

    def __init__(self):
        super(Connect4_Game, self).__init__()
        self.last_move = None
        self.turn = "Red"

    def __str__(self):
        transposed = []
        for i in range(7):
            transposed.append([row[i] for row in self.grid])
        ret = ""
        for row in transposed:
            ret += str(row) + "\n"
        return ret

    def add(self,color="",col=-1):
        if color == "R" or color == "B":
            if self.add_piece(color,col):
                self.last_move = tuple([color,col])
                self.turn = "Black" if self.turn == "Red" else "Red"
                return
            else:
                raise AttributeError("Invalid column: " + str(col))
        raise AttributeError("Invalid color: " + color)


    # just need to check the around the last move
    def check_win_scenario(self):
        color = self.last_move[0]
        col = self.last_move[-1]
        row = self.grid[col].index(color)
        win_scenario = color + color + color + color
        fours = [""]*8
        for i in range(4):
            # checking right horizontal win
            try:
                let = self.grid[col+i][row]
                fours[0] += let
            except IndexError:
                pass
            # checking left horizontal win
            try:
                let = self.grid[col-i][row]
                fours[1] += let
            except IndexError:
                pass
            # checking downward vertical win
            try:
                let = self.grid[col][row+i]
                fours[2] += let
            except IndexError:
                pass
            # checking upward vertical win
            try:
                let = self.grid[col][row-i]
                fours[3] += let
            except IndexError:
                pass
            # checking right downward diagonal win
            try:
                let = self.grid[col+i][row+i]
                fours[4] += let
            except IndexError:
                pass
            # checking left upward diagonal win
            try:
                let = self.grid[col-i][row-i]
                fours[5] += let
            except IndexError:
                pass
            # checking right upward diagonal win
            try:
                let = self.grid[col+i][row-i]
                fours[6] += let
            except IndexError:
                pass
            # checking left downward diagonal win
            try:
                let = self.grid[col-i][row+i]
                fours[7] += let
            except IndexError:
                pass
        for four in fours:
            if four == win_scenario:
                return True
        return False

    def is_full(self):
        return len(self.valids) == 0

    def get_valids(self):
        return self.valids
