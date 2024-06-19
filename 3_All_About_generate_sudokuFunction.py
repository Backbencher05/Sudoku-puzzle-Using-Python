#1: This imports the random module, which will be used to shuffle lists randomly.
import random

"""
2:
This defines the generate_sudoku function. base is set to 3,which is the base size of a standard Sudoku block (3x3). 
side calculates the full side length of the Sudoku grid (9x9).
"""
def generate_sudoku():
    base = 3
    side = base * base

    """
    3:
    This defines a nested function pattern, which calculates the value to be placed in each cell of the Sudoku 
    board based on its row (r) and column (c). This function ensures that each number appears exactly once in 
    each row, column, and 3x3 block in the initial solved Sudoku board.
    """
    def pattern(r, c): 
        return (base * (r % base) + r // base + c) % side
    
    """
    4:
    This defines a nested function shuffle, which takes a sequence s and returns a new list with the elements randomly shuffled. 
    random.sample(s, len(s)) achieves this by selecting all elements of s in random order.
    """
    def shuffle(s): 
        return random.sample(s, len(s))

    # This creates a range object rBase which represents the numbers 0, 1, and 2.
    rBase = range(base)
    """
    5:
    These lines generate lists rows and cols that represent the row and column indices for the Sudoku board.
    They are created by shuffling the base ranges and combining them in a specific way to ensure the pattern function 
    can produce a valid Sudoku solution
    """
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]

    # This shuffles the numbers 1 through 9. The nums list will be used to fill the Sudoku board with these shuffled numbers, 
    # ensuring the solution is randomized.
    nums = shuffle(range(1, base * base + 1))

    """
    This creates the board as a list of lists (a 2D array). It fills the board using the pattern function to determine the 
    correct value for each cell, ensuring a valid Sudoku solution.
    """
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    """
    side * side calculates the total number of squares on the board (81). empties calculates the number of cells that will
    be set to 0 (empty) to create the puzzle. Here, 3/4 of the cells are made empty.
    """
    squares = side * side
    empties = squares * 3 // 4

    """
    This loop iterates over a randomly selected set of positions in the board, making empties number of cells empty (set to 0).
    The random.sample(range(squares), empties) generates a list of random unique positions on the board to empty. p // side gives 
    the row index, and p % side gives the column index.
    """
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    # Finally, the function returns the generated Sudoku board with empty cells, ready to be used as a puzzle.
    return board







