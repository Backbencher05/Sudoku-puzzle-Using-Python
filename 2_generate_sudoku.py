import random

def generate_sudoku():
    base = 3
    side = base * base

    #create pattern
    def pattern(r, c): 
        return (base * (r % base) + r // base + c) % side
    
    # generate the numbers
    # sample(): Returns a given sample of a sequence
    def shuffle(s): 
        return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    # generate
    nums = shuffle(range(1, base * base + 1))

    # create board for Row and column wise
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    for line in board:
        print(line)
    
    squares = side * side
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

sudoku = generate_sudoku()
print_board(sudoku)
