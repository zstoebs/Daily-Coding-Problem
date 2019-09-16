"""
@author Zach Stoebner
@date 9-16-2019
@descrip The Tower of Hanoi is a puzzle game with three
  rods and n disks, each a different size.

All the disks start off on the first rod in a stack.
They are ordered by size, with the largest disk on the
bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from
the first rod to the last rod while following these rules:

You can only move one disk at a time.
A move consists of taking the uppermost disk from one
of the stacks and placing it on top of another stack.
You cannot place a larger disk on top of a smaller disk.

Write a function that prints out all the steps necessary
to complete the Tower of Hanoi. You should assume that
the rods are numbered, with the first rod being 1, the
second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
"""

#tower_of_hanoi class
#wrapper to solve Towers of Hanoi puzzle
#https://www.tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm
"""
START
Procedure Hanoi(disk, source, dest, aux)

   IF disk == 1, THEN
      move disk from source to dest
   ELSE
      Hanoi(disk - 1, source, aux, dest)     // Step 1
      move disk from source to dest          // Step 2
      Hanoi(disk - 1, aux, dest, source)     // Step 3
   END IF

END Procedure
STOP
"""
class tower_of_hanoi:

    def __init__(self,n_disks=3):
        self.n_disks = n_disks
        self.rods = [[x for x in range(n_disks)],[],[]]

    def solve(self):
        self.__solver(self.n_disks-1)

    def __move(self,disk,source,dest):
        self.rods[source].remove(disk)
        self.rods[dest].append(disk)
        print(f"Move {disk+1} to {dest+1}")

    def __solver(self,disk,source=0,aux=1,dest=2):

        if disk == 0:
            self.__move(disk,source,dest)
        else:
            self.__solver(disk-1,source,dest,aux)
            self.__move(disk,source,dest)
            self.__solver(disk-1,aux,source,dest)

### TESTS
t1 = tower_of_hanoi()
t1.solve()
"""
Move 1 to 3
Move 2 to 2
Move 1 to 2
Move 3 to 3
Move 1 to 1
Move 2 to 3
Move 1 to 3

"""
