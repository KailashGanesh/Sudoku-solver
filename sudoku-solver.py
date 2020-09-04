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

b2 =[[1,2,3],[1,2,3],[1,2,3]]
# function to print the board in cli
def printBoard(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - ")
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
def is_valid_move(board, pos, num):
    row, col = pos

    # checking row
    if num in board[row]:
        return False

    # checking column
    for i in range(len(board)):
        if num == board[i][col]:
            return False
    
    # checking the box
    box_x = row // 3
    box_y = col // 3

    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3,box_x*3 + 3):
            if board[i][j] == num:
                return False
    return True




# slove with backtracking algo
printBoard(board)
print(find_empty_spot(board))