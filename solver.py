def solve(board):
    '''
    Purpose: Solve the given sudoku board
    Parameters: board(2d array of ints)
    Return: bool if the board can be solved
    '''
    space = emptySpace(board)

    #logic for if there is an empty space or not
    if space:
        x,y = space
    else:
        return True
    
    for i in range(1,10):
        if valid(board,x,y,i):
            board[x][y] = i

            if solve(board):
                return True
            
            board[x][y] = 0
    
    return False


def emptySpace(board):
    '''
    Purpose: spots open spaces in the board and returns position of the empty space
    Parameter: board(2d array of ints)
    Return: tuple if an empty position is found
    '''
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j)
    
    return None


def valid(board:list, x:int, y:int, target) -> bool:
    '''
    Purpose: Checks if a number placed in the empty spot is valid
    Parameters: board(2d array of list), x(integer x coordinate), y(integer y coordinate), target(integer number being placed into empty spot)
    Returns: bool value if the number is valid or not
    '''

    #checks rows and columns
    for i in range(len(board)):
        if (board[i][y] == target and x!=i) or (board[x][i] == target and y!=i):
            return False
    
    #need to check 3x3 box now
    bo_x_len = x//3
    bo_y_len = y//3

    for i in range(bo_x_len*3, bo_x_len*3 + 3):
        for j in range(bo_y_len*3, bo_y_len*3 + 3):
            if board[i][j] == target and i!=x and j!=y:
                return False

    return True
            

def print_board(board:list) -> None:
    '''
    Purpose: prints the Sudoku board
    Parameters: board(2d array of ints)
    Returns: Nothing
    '''
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()
        
#Example boards used
board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

board2 = [
    [0,0,3,0,2,0,6,0,0],
    [9,0,0,3,0,5,0,0,1],
    [0,0,1,8,0,6,4,0,0],
    [0,0,8,1,0,2,9,0,0],
    [7,0,0,0,0,0,0,0,8],
    [0,0,6,7,0,8,2,0,0],
    [0,0,2,6,0,9,5,0,0],
    [8,0,0,2,0,3,0,0,9],
    [0,0,5,0,1,0,3,0,0]
]

if solve(board2):
    print_board(board2)
else:
    print("Board cannot be solved")