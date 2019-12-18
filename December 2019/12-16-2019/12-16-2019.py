"""
@author Zach Stoebner
@date 12-16-2019
@descrip Connect 4 is a game where opponents take turns dropping red or black discs into a
7 x 6 vertically suspended grid. The game ends either when one player creates a line of
four consecutive discs of their color (horizontally, vertically, or diagonally), or when
there are no more spots left in the grid.

Design and implement Connect 4.
"""

from Connect4 import Reactor as R

def main():

    eh = R.Event_Handler()
    reactor = R.Reactor()
    reactor.add_event_handler(eh)
    reactor.run_event_loop()

if __name__ == "__main__":
    main()
