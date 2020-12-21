import pygame, sys
from sudokuSolver import *

def drawGrid(grid,screen,board):
    '''
    parm: int - the grid size (for 9*9 give 9), pygame screen, the sudoku board
    it draws lines every 3 blocks, grids, and the text of the sudoku board
    '''
    blockSize = int(size[0]/grid) # width/no. of grids
    for x in range(grid):
        if x % 3 == 0 and x != 0:
           line_width = 5
        else:
            line_width = 1
        pygame.draw.line(screen,black,(0, x*blockSize),(size[0], x*blockSize), line_width) 
        pygame.draw.line(screen,black,(x*blockSize,0),(x*blockSize, size[0]), line_width) 

        for y in range(grid):
            rect = pygame.Rect(x*blockSize, y*blockSize,blockSize,blockSize)
            pygame.draw.rect(screen,black,rect,1)
            if board[y][x]:
                text = myfont.render(str(board[y][x]),True,black)
            else:
                text = myfont.render(" ",True,black)
            screen.blit(text, (x*blockSize+20,y*blockSize+9))

def mouseClick(pos,screen):
    '''
    parm: click position and screen 
    return: index of grid click, returns False when not click in grid
    how: the grind is drawn using width/no. of cols (here: 540/9 which is 60)
    so mouse click pos divided by 60 gives us the grid index which was clicked.
    '''
    x = int(pos[0]//(size[0]/9))
    y = int(pos[1]//(size[0]/9))
    if x < 9 and y < 9:
        print(pos)
        print(board[y][x])
        return y,x
    return False

pygame.font.init()
pygame.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
size = width, heigh = 540,600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
boxSelected = False # is any box selected in the grid
val = 0

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
boardBackup = [
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
print_board(board)
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            index = mouseClick(pos,screen)
            if index != False:
                y,x = index
                boxSelected = True
        if event.type == pygame.KEYDOWN: 
            print(event.key)
            if event.key == 120: # x key quits app
                sys.exit()
            if event.key == pygame.K_1: 
                val = 1
            if event.key == pygame.K_2: 
                val = 2    
            if event.key == pygame.K_3: 
                val = 3
            if event.key == pygame.K_4: 
                val = 4
            if event.key == pygame.K_5: 
                val = 5
            if event.key == pygame.K_6: 
                val = 6 
            if event.key == pygame.K_7: 
                val = 7
            if event.key == pygame.K_8: 
                val = 8
            if event.key == pygame.K_9: 
                val = 9  
            if event.key == pygame.K_SPACE: # space key sloves full board
                board = boardBackup
                solve_board(board)
                boxSelected = False
                pygame.display.update()
            if event.key == pygame.K_LEFT or event.key == 104:  # leftkey or h
                if boxSelected:
                    if x == 0: # if can't go left anymore start at right side
                        x = 8
                    else:
                        x-= 1
                else:
                    y = 0
                    x = 0
                    boxSelected = True
            if event.key == pygame.K_RIGHT or event.key == 108: # rightkey or l
                if boxSelected:
                    if x == 8:
                        x = 0
                    else:
                        x+= 1
                else:
                    y = 0
                    x = 0
                    boxSelected = True
            if event.key == pygame.K_UP or event.key == 107: # upkey or k
                if boxSelected:
                    if y == 0:
                        y = 8
                    else:
                        y-= 1
                else:
                    y = 0
                    x = 0
                    boxSelected = True
            if event.key == pygame.K_DOWN or event.key == 106: # downkey or j
                if boxSelected:
                    if y == 8:
                        y = 0
                    else:
                        y += 1
                else:
                    y = 0
                    x = 0
                    boxSelected = True
            if event.key == 114: # r key to gen new board
                board = make_board(board)
                boardBackup = board


    screen.fill(white)
    drawGrid(9,screen,board)

    if boxSelected:
        #y,x = index
        rect = pygame.Rect(x*60,y*60,60,60)
        pygame.draw.rect(screen,red,rect,5)
        if val:
            if board[y][x] == 0:
                if is_valid_move(board, val, (y,x)):
                    board[y][x] = val
                else:
                    print("wrong")
                val = 0
            else:
                val = 0

    pygame.display.update()
