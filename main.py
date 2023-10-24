# Tic Tac Toe

# Author : Prajjwal Pathak (pyguru)
# Date : Thursday, 28 October, 2021

import random
import pygame
from objects import Rect, generate_boxes, create_board
from logic import isBoardFull, check_win

pygame.init()
SCREEN = WIDTH, HEIGHT = (288, 512)

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 60

# COLORS *********************************************************************

WHITE = (225,225,225)
BLACK = (0, 0, 0)
GRAY = (32, 33, 36)
BLUE = (0, 90, 156)
ORANGE = (208, 91, 3)

# IMAGES *********************************************************************

bg1 = pygame.image.load('Assets/bg1.png')
bg1 = pygame.transform.scale(bg1, (WIDTH, HEIGHT-10))

bg2 = pygame.image.load('Assets/bg2.png')
bg2 = pygame.transform.scale(bg2, (WIDTH, HEIGHT-10))

replay_image = pygame.image.load('Assets/replay.png')
replay_image = pygame.transform.scale(replay_image, (36, 36))
replay_rect = replay_image.get_rect()
replay_rect.x = WIDTH - 110
replay_rect.y = 210

# BOARD FUNCTIONS ************************************************************

board = create_board()
box_list = generate_boxes()
players = ['X', 'O']
current_player = random.randint(0, 1)
text = players[current_player]

# FONTS **********************************************************************

scoreX = 0
scoreO = 0

font1 = pygame.font.Font('Fonts/PAPYRUS.ttf', 17)
font2 = pygame.font.Font('Fonts/CHILLER.ttf', 30)
font3 = pygame.font.Font('Fonts/CHILLER.ttf', 40)

tic_tac_toe = font2.render('Tic Tac Toe', True, WHITE)

# VARIABLES ******************************************************************

result = None
line_pos = None
click_pos = None

running = True
while running:
	if result:
		win.blit(bg2, (0,5))
	else:
		win.blit(bg1, (0,5))

	pygame.draw.rect(win, BLUE, (10, 10, WIDTH-20, 50), border_radius=20)
	pygame.draw.rect(win, WHITE, (10, 10, WIDTH-20, 50), 2, border_radius=20)
	win.blit(tic_tac_toe, (WIDTH//2-tic_tac_toe.get_width()//2,17))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		
	pygame.display.update()
pygame.quit()