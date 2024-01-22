def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple for(None, None) if there is none

    # keep in mind that we are using 0,0 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, 3 ...8
            if puzzle[r][c] ==  -1:
                return r, c
            
    return None, None # if no spaces in the puzzle are empty (-1)


def solve_sudoku(puzzle):
    # solve sudoku with a backtracking technique
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exits
    # mutates puzzle to be the solution  (if the solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
