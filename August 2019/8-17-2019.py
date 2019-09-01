"""
Author: Zach Stoebner
Created on: 8-17-2019
Descrip:

Given a 2D board of characters and a word,
find if the word exists in the grid.

The word can be constructed from letters of
sequentially adjacent cell, where "adjacent"
cells are those horizontally or vertically
neighboring. The same letter cell may not be
used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true,
exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.

"""
#exists
#Note: returns bool of word existence in 2D board
#to get dims of board, need length of outer list and length of each inner list
#can do a recursive DFS
def exists(board,word):

    n_rows = len(board)
    n_cols = len(board[0])

    def helper(row,col,visited=[],word_ind=1):

        if (row,col) in visited:
            return False
        elif word_ind >= len(word):
            return True
        else:
            visited.append(tuple([row,col]))
            up = down = left = right = False
            if row+1 < n_rows and board[row+1][col] == word[word_ind]:
                down = helper(row+1,col,visited,word_ind+1)
            if row-1 >= 0 and board[row-1][col] == word[word_ind]:
                up = helper(row-1,col,visited,word_ind+1)
            if col+1 < n_cols and board[row][col+1] == word[word_ind]:
                right = helper(row,col+1,visited,word_ind+1)
            if col-1 >= 0 and board[row][col-1] == word[word_ind]:
                left = helper(row,col-1,visited,word_ind+1)
            return (up or down or left or right)

    #finding start locations
    start = word[0]
    for row in range(n_rows):
        if start in board[row]:
            for col in range(n_cols):
                if start == board[row][col]:
                    if helper(row,col):
                        return True

    return False

### TESTS
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(exists(board, "ABCCED")) #true
print(exists(board, "SEE")) #true
print(exists(board, "ABCB")) #false

### ADMIN SOLUTION
def search(board, row, col, word, index, visited):
    def is_valid(board, row, col):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

    if not is_valid(board, row, col):
        return False
    if visited.contains((row, col)):
        return False
    if board[row][col] != word[index]:
        return False
    if index == len(word) - 1:
        return True

    visited.add((row, col))

    for d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        if search(board, row + d[0], col + d[1], word, index + 1):
            return True

    visited.remove((row, col))  # Backtrack

    return False

def find_word(board, word):
    int M = len(board)
    int N = len(board[0])

    for row in range(M):
        for col in range(N):
            visited = set()
            if search(board, row, col, word, 0, visited):
                return True
