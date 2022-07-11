"""
Math 560
Project 4
Fall 2021

Partner 1: Beibei Wu (NetID: mw515)
Partner 2: Libo Zhang (NetID: lz200)
Date: November 10, 2021
"""

# Import p4tests.
from p4tests import *

# Indicate 80 characters in a line of code.
###############################################################################

"""
ED: the edit distance function

INPUT:
src: source string
dest: destination string
prob: option ('ED' or 'ASM')

OUTPUT:
dist: the total number of edits to convert src to dest
edits: tuples of all edits
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    # Raise an exception if prob is neither 'ED' nor 'ASM'.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')

    # Construct 2-D cumulative table
    ## Initialization
    edits = []
    row = len(src)
    col = len(dest)

    ## (row + 1) * (col + 1) matrix for saving cumulated results
    two_dimen = [[0 for j in range(col + 1)] for i in range(row + 1)]

    # Base Cases for Edit Distance ('ED').
    if prob == 'ED':
        # Initialize the first column of 'ED'
        # Source string not empty, while Destination string empty
        # Source string edit - Delete
        for i in range(row + 1):
            two_dimen[i][0] = i
        # Initialize the first row of 'ED'
        # Source string empty, while Destination string not empty
        # Source string edit - Insert
        for j in range(col + 1):
            two_dimen[0][j] = j

    # Base Cases for Approximate String Matching ('ASM').
    if prob == 'ASM':
        for i in range(row + 1):
            two_dimen[i][0] = i
        # For the ASM problem, we ignore any insertions that
        # would need to occur to the left of the first edit.
        for j in range(col + 1):
            # The only difference between ASM and ED is one of 
            # the base cases: The first row of the table should
            # be filled with 0s for the ASM problem.
            two_dimen[0][j] = 0

    # Construct two dimensional table
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            # Match
            if src[i - 1] == dest[j - 1]:
                # Make 0 edit
                two_dimen[i][j] = two_dimen[i - 1][j - 1]
                continue
            # Insert 
            ins = two_dimen[i][j-1]

            # Substitute
            sub = two_dimen[i - 1][j - 1]

            # Delete
            rem = two_dimen[i -  1][j]

            # Make 1 edit
            two_dimen[i][j] = min(ins, sub, rem) + 1

    # Write dist result
    dist = two_dimen[row][col]

    # Reconstruct solution
    i = row
    j = col
    while (i > 0 and j > 0):
        if two_dimen[i][j] - 1 == two_dimen[i][j-1]: 
            ## insert, use dest's letter                     
            edits.append(('insert', dest[j - 1], i))
            ## j update                                                   
            j -= 1
        elif two_dimen[i][j] - 1 == two_dimen[i - 1][j - 1]:
            ## substitute, use dest's letter
            edits.append(('sub', dest[j - 1], i - 1))
            j -= 1
            i -= 1
        elif two_dimen[i][j] - 1 == two_dimen[i - 1][j]:   
            ## delete, use src's letter               
            edits.append(('delete', src[i - 1], i - 1))                                    
            i -= 1                                                            
        else:
            ## match, use src's letter                                                          
            edits.append(('match', src[i - 1], i - 1))
            i -= 1
            j -= 1
    ## if i <= 0 and j <= 0:
    ##     pass: come to upper left corner
    if i <= 0 and j > 0:
        ## come to the first row
        ## still needs several insertions
        while j > 0:
            edits.append(('insert', dest[j - 1], 0))
            j -= 1
    elif i > 0:
        ## come to the first column
        while i > 0:
            edits.append(('delete', src[i - 1], i - 1))
            i -= 1

    ## print(edits)
    return dist, edits



###############################################################################
# Indicate 80 characters in a line of code.

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
