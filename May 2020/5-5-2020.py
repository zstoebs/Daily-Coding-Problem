"""
@author Zach Stoebner
@date 5-5-2020
@details You have access to ranked lists of songs for various users.
Each song is represented as an integer, and more preferred songs appear earlier in each list.
For example, the list [4, 1, 7] indicates that a user likes song 4 the best,
followed by songs 1 and 7.

Given a set of these ranked lists, interleave them to create a playlist that satisfies
everyone's priorities.

For example, suppose your input is {[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}.
In this case a satisfactory playlist could be [2, 1, 6, 7, 3, 9, 5].
"""

# playlist
# interleaves a playlist that satisfies the orderings of all passed lists
# Assumption 1: input is a list of lists of ints (can't be built-in set of lists b/c lists aren't hashable)
# Assumption 2: no contradictions in input s.t. one person likes A over B while another likes B over A
# Complexity: O(N)
def playlist(lsts: list):

    """
    Iterative algorithm:
    1. for each list in input set, find the songs that aren't already in the playlist
    2. insert the new songs into the playlst at the indices following the previous song in the current list
    """

    playlst = []
    for lst in lsts:

        # create a lst of songs in lst that aren't in playlst
        new_songs = [x for x in lst if x not in playlst]

        # if not the empty set
        if new_songs != []:

            # if all the songs are new, just append them to playlst
            if new_songs == lst:
                playlst += new_songs

            # o/w
            else:
                for song in new_songs:
                    ind = lst.index(song) # if input assumption is correct, song is in lst so I won't get a ValueError

                    # new first song so just insert in front
                    if ind == 0:
                        playlst.insert(0,song)

                    # new last song so insert at the end to not accidentally contradict previous orderings
                    elif ind == len(lst)-1:
                        playlst += [song]

                    # o/w insert after previous song in lst (aka before the song following the previous song in playlst)
                    else:
                        playlst.insert(playlst.index(lst[ind-1])+1, song)
    return playlst

### TESTS\
print(playlist([[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]))
