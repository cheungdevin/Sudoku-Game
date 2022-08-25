"""
Sudoku Game by Devin Cheung
"""

from typing import Optional

# Constants
Board = list[list[Optional[int]]]

HELP = "H" 
QUIT = "Q"
CLEAR = "C"

VERTICAL_WALL = "|"
HORIZONTAL_WALL = "-"
BLANK = " "

START_GAME_PROMPT = "Please insert the name of a board file: "
INPUT_PROMPT = "Please input your move: "
INVALID_MOVE_MESSAGE = "That move is invalid. Try again!"
WIN_MESSAGE = "Congratulations, you won!"
NEW_GAME_PROMPT = "Would you like to start a new game (y/n)? "
HELP_MESSAGE = "Need help?\nH = Help\nQ = Quit\nHint: Make sure each row, column, and square contains only one of each number from 1 to 9."

def load_board(filename: str) -> str:
    """ Reads a board file and creates a string containing all the rows in order.

    Parameters:
        filename: The path to the game file

    Returns:
        A single string containing of all rows in the board.

    >>> load_board("../boards/board_one.txt")
    '68513  477      1  1 764 5 9   7 5 48 1  9 724 3  6      42739  4 9   681 7   4  '
    """
    board = ""
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('-'):
                line = line.replace("|","")
                line = line.replace("\n","") # BW file.readlines() should do this
                board += line
    return board

# Returns True if the given (row, column) position contains None and False otherwise.
def is_empty(position: tuple[int, int], board: Board) -> bool:
    if board[position[0]][position[1]] is None:
        return True
    return False

# Updates the board at the provided (row, column) position with the provided value.
def update_board(position: tuple[int, int], value: Optional[int], board: Board) -> None:
    board[position[0]][position[1]] = value

# Updates the board to clear the cell at the provided (row, column) position.
def clear_position(position: tuple[int, int], board: Board) -> None:
    board[position[0]][position[1]] = None

# Converts the raw board from a string of characters into a list of 9 lists. 
def read_board(raw_board: str) -> Board: 
    board = []
    j = 0
    temp = []
    for i in range(81):
        if raw_board[i] is BLANK:
            temp.append(None)
        else:   
            temp.append(int(raw_board[i]))
        if((i+1)%9==0):
            board.append(temp)
            temp = []
    
    return board

# Displays the puzzle in a user-friendly format.
def print_board(board: Board) -> None:
    j = 0
    for i in range(9):
        if i%3==0 and i!=0:
                print(HORIZONTAL_WALL*11)
        for j in range(9):
            if j%3==0 and j!=0:
                print(VERTICAL_WALL,end='')
            if board[i][j] is None:
                print(BLANK,end='')
            else:
                print(board[i][j],end='')
        print('',i)
    print("\n012 345 678")

# Returns True if the game is won, False otherwise.
def has_won(board: Board) -> bool:

    # Check if every index filled with number
    for row in board:
        if None in row:
            return False
    
    # Check if every row filled with 1-9 without repeating
    for row in board:
        for i in range(1,10):
            if i not in row:
                return False

    # Check if every column filled with 1-9 without repeating   
    for i in range(9):
        column = []
        for row in board:
            column.append(row[i])
        for j in range(1,10):
            if j not in column:
                return False
    
    # Check if every 3*3 box filled with 1-9 without repeating   
    for row in range(0,9,3):
        for col in range(0,9,3):
            sub_board = []
            for i in range(row,row+3):
                for j in range(col, col+3):
                    if board[i][j] != 0:
                        sub_board.append(board[i][j])
            for j in range(1,10):
                if j not in sub_board:
                    return False
    return True

def main() -> None:
    new_game = 'y'

    while new_game is not None:
        # read file and initialize the board setting
        if new_game == 'y':
            filename = input(START_GAME_PROMPT)
            str = load_board(filename)
            # str = load_board("boards/board_one.txt")
            # str = "12345678923456789134567891245678912356789123467891234578912345689123456791234567 "
            board = read_board(str)
            original_board = read_board(str)
            print_board(board)
            user_input = None
            new_game = 'n'
        
        user_input = input(INPUT_PROMPT)

        # set user input to upper case
        # if 'a'<= user_input <='z':
        #     user_input = chr(ord(user_input)-32)
        if user_input == 'h':
            user_input = 'H'
        if user_input == 'q':
            user_input = 'Q'

        # QUIT option
        if user_input is QUIT:
                break
        
        # HELP option
        elif user_input is HELP:
            print(HELP_MESSAGE)
            print()
            print_board(board)
        else:
            position = [int(user_input[0]),int(user_input[2])]
            if is_empty(position,original_board):
                value = user_input[4]

                # CLEAR option
                if value is CLEAR:
                    clear_position(position,board)
                else:
                    # update the board
                    update_board(position,int(value),board)
                print_board(board)

                # check if user win
                if has_won(board):
                    print(WIN_MESSAGE)
                    new_game = input(NEW_GAME_PROMPT)
                    if(new_game) == 'n':
                        break
            else:
                # invalid input
                print(INVALID_MOVE_MESSAGE)
                print_board(board)


if __name__ == "__main__":
    main()
