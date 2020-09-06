board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
# function to print the board in cli
def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - ")
        for j in range (len(board[0])):
            
            if j%3 == 0 and j != 0:
                print("| ",end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j]," ", end="")

# find empty spot in the board
def find_empty_spot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return False

# is this a valid move
def is_valid_move(board, num, pos):
    row,col = pos
    # checking row
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    # checking column
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False
    
    # checking the box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3,box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True



# slove with backtracking algo
def solve_board(board):
    spot = find_empty_spot(board)

    if spot == False:
        return True
    else:
        row, col = spot

    for i in range(1,10):
        if is_valid_move(board,i,(row,col)):
            board[row][col] = i

            if solve_board(board):
                return True

            board[row][col] = 0
    return False

def make_board(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            for m in range (1,10):
                if is_valid_move(board,i,(i,j)):
                    board[i][j] = m

# b1 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
# make_board(b1)
# print_board(b1)
print_board(board)
solve_board(board)
print("solved")
print_board(board)