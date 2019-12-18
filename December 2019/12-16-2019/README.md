# Connect4
### From DCP for 12-16-2019.py

## About
My design and implementation for a CLI Connect4 game. I employed some basic design patterns:
- the Reactor pattern
- the Adapter pattern
- (arguably) the Strategy pattern is implemented[-able] via the Event_Handler class

Potential updates include (prioritized order):
- Continuous play after a win
- Don't shut the program down after an invalid input
- Peer-to-peer network play
- Beautification of the interface

## Usage
From the command line:
1. Navigate to the directory
2. Input command: `python 12-16-2019.py`
3. Choose from the playable columns or type *-1* to quit
