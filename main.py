from itertools import product

ROW_COUNT, COL_COUNT = 9, 9
EMPTY_CELL = 0
NUM_RANGE = range(1, 10)


def print_sudoku(puzzle: list):
    for row in puzzle:
        print(f'{row}')


def solve_sudoku(puzzle: list) -> list:
    # compile lists for missing numbers
    missing_row_list = get_row_list(puzzle)
    missing_col_list = get_col_list(puzzle)
    missing_square_list = get_square_list(puzzle)

    empty_cell_count = count_number(puzzle, EMPTY_CELL)
    total_count = ROW_COUNT * COL_COUNT
    ratio = empty_cell_count / total_count

    puzzle_iters = 0

    while empty_cell_count > 0:
        puzzle_iters += 1
        # iterate over all cells in puzzle
        for row, col in product(range(ROW_COUNT), range(COL_COUNT)):
            # if cell empty, try finding if a unique match can be found
            if puzzle[row][col] == EMPTY_CELL:
                square = (row // 3) * 3 + col // 3
                # get list of numbers that are missing in rows, cols and square
                match_num_list = [num for num in NUM_RANGE if
                                  num in missing_row_list[row] and num in missing_col_list[col] and num in
                                  missing_square_list[square]]
                # print(f'Total missing {zero_count}, Missing numbers at [{row}][{col}]: {match_list}')
                # if unique missing number found
                if len(match_num_list) == 1:
                    add_num = match_num_list[0]
                    assert add_num != EMPTY_CELL, 'Cannot add {EMPTY_CELL} to cell'
                    puzzle[row][col] = add_num
                    empty_cell_count -= 1
                    print(f'Added missing number {add_num} at puzzle[{row}][{col}] - {empty_cell_count} more missing')
                    # update lists
                    missing_row_list[row].remove(add_num)
                    missing_col_list[col].remove(add_num)
                    missing_square_list[square].remove(add_num)

    assert empty_cell_count == 0, f'{empty_cell_count} empty cells remaining'
    print(f'Solution found: {puzzle_iters} puzzle iterations required')
    return puzzle


def count_number(puzzle: list, num: int) -> int:
    count = 0
    for row in puzzle:
        count += row.count(num)
    return count


def get_row_list(puzzle) -> list:
    missing_row_list = list()

    for row in puzzle:
        missing_row = [val for val in NUM_RANGE if val not in row]
        # missing number list in row
        missing_row_list.append(missing_row)

    return missing_row_list


def get_col_list(puzzle) -> list:
    missing_col_list = list()

    for col_num in range(9):
        # create row of columns
        col = [puzzle[row_num][col_num] for row_num in range(9)]
        # missing number list in column
        missing_col = [val for val in NUM_RANGE if val not in col]
        missing_col_list.append(missing_col)

    return missing_col_list


def get_square_list(puzzle) -> list:
    missing_square_list = list()

    for square_num in range(9):
        square = list()
        # create a list for all numbers in a quadrant
        for row in range(3 * (square_num // 3), 3 * (square_num // 3) + 3):
            for col in range(3 * (square_num % 3), 3 * (square_num % 3) + 3):
                # print(f'puzzle[{row}][{col}] = {puzzle[row][col]}')
                square.append(puzzle[row][col])

        # print(f'square {square_num}: {square}')
        # missing number list in quadrant
        missing_square = [val for val in NUM_RANGE if val not in square]
        missing_square_list.append(missing_square)

    return missing_square_list


def print_list(num_list: list, caption: str = ''):
    print(f'{caption}')
    for val_num, val in enumerate(num_list, 1):
        print(f'{val_num}: {val}')


def main():
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    print_sudoku(puzzle)
    solution = solve_sudoku(puzzle)
    print_sudoku(solution)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
