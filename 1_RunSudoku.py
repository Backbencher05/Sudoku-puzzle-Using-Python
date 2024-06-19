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

    squares = side * side
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    sudoku = generate_sudoku()
    print("Generated Sudoku Puzzle:")
    print_board(sudoku)

    while True:
        row = int(input("Enter row (0-8): "))
        col = int(input("Enter column (0-8): "))
        num = int(input("Enter number (1-9): "))

        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            print("Updated Sudoku Puzzle:")
            print_board(sudoku)
        else:
            print("Invalid move! Try again.")

        if solve(sudoku):
            print("Congratulations! You solved the puzzle!")
            break

if __name__ == "__main__":
    main()
