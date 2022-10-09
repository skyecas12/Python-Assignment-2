# import libraries here. Use the following ones only.
import time, sys, random


# add your implementation of the required functions here


def update_board(row, column, guess):

    return


# def game_state(grid, row, column):

    # if i in either grid, row or column is False, will return as not solved.
    # if grid and row and column is is_valid(grid, row, column):
        # print("The board has been solved successfully, congratulations!")
    # else:
        # print("The board has NOT been solved.")
    # return


def is_valid(grid, number, position):
    # loops through every row,checking all elements
    # within each row so that the numbers do not collide with each other
    for i in range(len(grid[0])):
        if grid[position[0]][i] == number and position[1] != i:
            return False

    # loops through every column within the grid to ensure no collision happens
    for i in range(len(grid)):
        if grid[i][position[1]] == number and position[0] != i:
            # checking all elements within each column, so that the numbers do not collide with each other.
            return False

    # checking the square of a position on the x_axis of the grid
    square_x = position[1] // 3
    # checking the square of a position on the y_axis of the grid
    square_y = position[0] // 3

    # multiplies the squares by 3, so it can check the elements across and down the other 3x3 grids.
    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            # multiplies by 3, so it can check all 3 of the 3x3 grids, and also adds 3 so -
            # - that adding 3 will mean, each 3x3 grid can be checked either down, or across 3.
            if grid[i][j] == number and (i, j) != position:
                # if the number is equal to what we add, -
                # then return false if it gives us the same number within a 3x3 grid,  row or column.
                return False

    return True


def find_empty_space(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # using i within a for i and j loop to look through the grid, for empty spaces.-
            if grid[i][j] == ' ':
                # if the function and grid detects an empty space with the row and column -
                # it will return the space to be filled later in computer play.
                return i, j
    return False


count = 0
# made a variable counter so we can use it in -
# - computer_play to count steps taken to complete sudoku.


def computer_play(grid):
    # References count as a global variable to be able -
    # - to be used outside the computer_play function as well as inside.
    global count
    full_board = find_empty_space(grid)
    if full_board is False:
        # if the full board is false, which refers to find_empty space function. -
        # - that means the board does not need to be completed as it has already been filled and solved.
        return True
    else:
        # if the full_board is not False, -
        # - then it must use the backtracking solving algorithm to solve the grid.
        row, column = full_board
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Using 9 strings to be able to fill our grid with any of the available strings in the list.
    for i in num_list:
        if is_valid(grid, i, (row, column)):
            grid[row][column] = i
            # if the position is valid to be available and not taken already,
            # - then fill the available position with a number from the list
            count += 1
            # add a number to the count if there has been a move taken place within the grid,
            # - move forward, or backtracked and replaced a number to move forward again.
            if computer_play(grid):
                # if computer play runs, allow it to return true as there is
                # - no empty spaces or colliding numbers within any 3x3 grids, -
                # - as well as columns or rows.
                return True
            else:
                # else if the computer_play does not return true, then it will need to backtrack to the number -
                # = which collides with a later number, =
                # = and attempt to retry the position with another available number to use.
                grid[row][column] = ' '

    return False


def human_play():
    return


def print_board(sudoku):
    for i in range(9):
        print(sudoku[i][0:3], '|', sudoku[i][3:6], '|', sudoku[i][6:9])
        if i == 5 or i == 2:
            print('-' * 51)


if __name__ == '__main__':

    # Don't change the layout of the following sudoku examples
    sudoku1 = [
        [' ', '1', '5', '4', '7', ' ', '2', '6', '9'],
        [' ', '4', '2', '3', '5', '6', '7', ' ', '8'],
        [' ', '8', '6', ' ', ' ', ' ', ' ', '3', ' '],
        ['2', ' ', '3', '7', '8', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', ' ', ' ', ' ', ' ', '9', ' '],
        ['4', ' ', ' ', ' ', '6', '1', ' ', ' ', '2'],
        ['6', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '4', ' ', ' ', ' ', '1', ' ', '7'],
        [' ', ' ', ' ', ' ', '3', '7', '9', '4', ' '],
    ]
    sudoku2 = [
        [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' '],
        ['7', '3', '4', ' ', '8', ' ', '1', '6', '2'],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', '3', '8'],
        ['5', '6', '8', ' ', ' ', '4', ' ', '1', ' '],
        [' ', ' ', '2', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', '8', ' ', ' ', '2', '5', '4'],
        [' ', '7', ' ', ' ', ' ', '2', '8', '9', ' '],
        [' ', '5', '1', '4', ' ', ' ', '7', '2', '6'],
        ['9', ' ', '6', ' ', ' ', ' ', ' ', '4', '5'],
    ]
    sudoku3 = [
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
        [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
        [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
        [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
        [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
        [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
        [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
    ]
    sudoku4 = [
        [' ', '4', '1', ' ', ' ', '8', ' ', ' ', ' '],
        ['3', ' ', '6', '2', '4', '9', ' ', '8', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '7', ' '],
        [' ', ' ', ' ', '4', '7', ' ', '2', '1', ' '],
        ['7', ' ', ' ', '3', ' ', ' ', '4', ' ', '6'],
        [' ', '2', ' ', ' ', ' ', ' ', ' ', '5', '3'],
        [' ', ' ', '7', ' ', '9', ' ', '5', ' ', ' '],
        [' ', ' ', '3', ' ', '2', ' ', ' ', ' ', ' '],
        [' ', '5', '4', ' ', '6', '3', ' ', ' ', ' '],
    ]

    # make sure 'option=2' is used in your submission
    option = 2

    if option == 1:
        sudoku = sudoku1
    elif option == 2:
        sudoku = sudoku2
    elif option == 3:
        sudoku = sudoku3
    elif option == 4:
        sudoku = sudoku4
    else:
        raise ValueError('Invalid choice!')

    # add code here to solve the sudoku

print_board(sudoku)
# prints original sudoku board, unsolved.
print(" =================================================")
start_time = time.time()
# starts the time taken of beginning the sudoku board just before the computer solves it.
computer_play(sudoku)
# calls the function computer play to run the Sudoku solver
print_board(sudoku)
# prints the sudoku board below computer_play, so it should be solved.
finish_time = time.time()
# finishes time taken to calculate the length of the sudoku board.
time = finish_time - start_time
print("The time taken to solve this board is: ", "%.4f" % time)
print("The total counts taken to solve this board was: ", count)

# prints both the time with 4 floating point format, as well -
# - as the amount of times a play was counted on the board by the computer


# print(game_state)
# user = input("Would you like the computer to run the sudoku again or end the program? Please say play or end.: ")
# if user is ("Play" or "PLAY" or "play"):
#     computer_play(sudoku)
#     print(sudoku)
# if user is ("End" or "END" or "end"):
#     sys.exit


