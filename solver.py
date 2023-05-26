def solve(board):
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
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j)
    
    return None


def valid(board:list, x:int, y:int, target) -> bool:
    
    #checks rows
    for i in range(len(board)):
        if board[i][y] == target and x!=i:
            print(i,y)
            return False

    #checks columns
    for i in range(len(board)):
        if board[x][i] == target and y!=i:
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
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()
        

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


# print_board(board)
# if valid(board,0,8):
#     print("!!!!!!!!!VALID!!!!!!!!!")
# else:
#     print("-----INVALID-----")



# print(len(board)) Rows
# print(len(board[0])) Columns