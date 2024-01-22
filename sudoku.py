def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple for(None, None) if there is none

    # keep in mind that we are using 0,0 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, 3 ...8
            if puzzle[r][c] ==  -1:
                return r, c
            
    return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # figures if the guess at the row/col of the puzzle is valid
    # return false if it is not, true if it is

    # let's start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # columns:
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i] [col])
    col_vals = [puzzle[i] for i in range(9)]
    if guess in col_vals:
        return False
    
    # and then the squeares
    # we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    # if we get here, these checks pass
    return True


def solve_sudoku(puzzle):
    # solve sudoku with a backtracking technique
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exits
    # mutates puzzle to be the solution  (if the solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    # step 2: if there us a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range (1, 10) is 1, 2, 3 ... 9
        #step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle:
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
            
            #step 5: if not valid OR if our guess does not solve the puzzle, then we need to
            # backtrack and try a new number
            puzzle[row][col] = -1 # resetting the guess

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVEABLE!!
    return False    

