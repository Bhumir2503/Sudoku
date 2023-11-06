"""
TO DO: 
1. Create new board each time
2. Create a Validator
3. Create a Solver
"""


import pygame
from generator import start
import random
import time
# Sample Sudoku puzzle
def board_builder():
    board = []
    solved_board = []
    x = start()
    k = 0
    for i in range(9):
        col = []
        sol_col = []
        for j in range(9):
            value = random.randint(1, 3)
            if(value == 1):
                sol_col.append(x[k].value)
                col.append(x[k].value)
            else:
                sol_col.append(x[k].value)
                col.append(0)
            k= k+1
        board.append(col)
        solved_board.append(sol_col)
    
    return [board, solved_board]


def regenerate():
    screen.fill(WHITE)
    x = start()
    k=0
    for i in range(9):
        for j in range(9):
            value = random.randint(1, 3)
            if(value == 1):
                solved_board[i][j] = x[k].value
                sudoku_board[i][j]= x[k].value
            else:
                solved_board[i][j] = x[k].value
                sudoku_board[i][j]= 0
            k= k+1


def solver():
    array = list(range(0, 81))
    random.shuffle(array)
    for i in range (81):
        row = array[i] // 9
        col  = array[i] % 9
        sudoku_board[row][col] = solved_board[row][col]
        time.sleep(0.1)
        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        pygame.display.update()

#draws the grid and buttons
def draw_grid():
    for i in range(GRID_SIZE + 1):
        thickness = LINE_WIDTH if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(450+75, 100, 150, 50))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(450+75, 275, 150, 50))
    text_surface = font.render("Regenerate", True, (255,255,255))
    screen.blit(text_surface, (450+75+10, 115))
    text_surface = font.render("Solver", True, (255,255,255))
    screen.blit(text_surface, (450+75+40, 290))


#Inital Inputs the number in the grid
def draw_numbers():
    k = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            num = sudoku_board[i][j]
            if num != 0:
                text = font.render(str(num), True, BLACK)
                x = j * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2
                y = i * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2
                screen.blit(text, (x, y))





def click_handler(pos):
    x, y = pos
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    # Handle cell click here
    if row < 9 and col < 9:
        if sudoku_board[row][col] == 0:
            input_number = input("Enter a number for this cell (1-9): ")
            try:
                input_number = int(input_number)
                if 1 <= input_number <= 9:
                    sudoku_board[row][col] = input_number
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
    elif x > 525 and x < 525+150 and y > 100 and y < 150:
        board = regenerate()
    elif x > 525 and x < 525+150 and y > 275 and y < 325:
        solver()
    else:
        pass


# Constants
WIDTH, HEIGHT = 450, 450
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_WIDTH = 2

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH +300, HEIGHT))
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.Font(None, 36)


# Board Builder
board = board_builder()

sudoku_board = board[0]
solved_board = board[1]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                click_handler(pygame.mouse.get_pos())

    screen.fill(WHITE)
    draw_grid()
    draw_numbers()
    pygame.display.update()

pygame.quit()

