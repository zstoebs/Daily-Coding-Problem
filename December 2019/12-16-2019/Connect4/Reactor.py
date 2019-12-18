"""
@author Zach Stoebner
@date 12-16-2019
@descrip Connect 4 is a game where opponents take turns dropping red or black discs into a
7 x 6 vertically suspended grid. The game ends either when one player creates a line of
four consecutive discs of their color (horizontally, vertically, or diagonally), or when
there are no more spots left in the grid.

Design and implement Connect 4.
"""

# a singleton reactor instance to run the continuous event loop for the game
class Reactor:

    # the singleton reactor instance
    class __Reactor:
        def __init__(self):
            self.dispatch_table = []
            self.running_event_loop = True

    instance = None
    def __init__(self):
        if not Reactor.instance:
            Reactor.instance = Reactor.__Reactor()

    def run_event_loop(self):

        while Reactor.instance.running_event_loop:
            for eh in Reactor.instance.dispatch_table:
                eh.handle_input()

    def end_event_loop():
        Reactor.instance.running_event_loop = False

    def add_event_handler(self, eh):
        Reactor.instance.dispatch_table.append(eh)

    # removes first instance of eh, if no event handler nothing happens
    def remove_event_handler(self,eh):
        if eh in Reactor.instance.dispatch_table:
            Reactor.instance.dispatch_table.remove(eh)

from Connect4 import Game

class Event_Handler:

    def __init__(self):
        self.prompted = False
        self.game = Game.Connect4_Game()
        self.input = None

    def prompt(self):
        print("Turn: ", self.game.turn)
        print("Choose from the valid columns: ", self.game.get_valids())
        print("Or type '-1' to exit")

    def get_input(self):
        self.input = input("> ")
        self.input = int(self.input)
        return self.input == -1 or self.input in self.game.get_valids()

    def handle_input(self):
        self.prompt()
        while not self.get_input():
            print("Error: Unknown input value ", self.input)

        if self.input == -1:
            Reactor.end_event_loop()
            return

        color = "R" if self.game.turn == "Red" else "B"
        self.game.add(color,self.input)
        print(self.game)
        if self.game.check_win_scenario():
            winner = "Red" if color == "R" else "Black"
            print("Winner is: ", winner)
            Reactor.end_event_loop()
