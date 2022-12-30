import pygame
from constants import *




button_list = [button1, button2, button3, button4, button5, button6]

surface2 = pygame.Surface((START_WINDOW_WIDTH, START_WINDOW_HEIGHT))

surface3 = pygame.Surface((START_WINDOW_WIDTH, START_WINDOW_HEIGHT))

#
pygame.init()
surface1 = pygame.display.set_mode((START_WINDOW_WIDTH, START_WINDOW_HEIGHT))
pygame.display.set_caption("Tres en raya - Pygame")
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)



running = True
while running:
    clock.tick(10)
    surface1.fill(LIGHT_GREY)
    surface2.fill(LIGHT_GREY)
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in button_list:
                if i.collidepoint(event.pos):
                    print("button clicked")
            if button_help.collidepoint(event.pos):
                surface1.blit(surface2, (0, 0))
                pygame.display.flip()
                print("I did it")
    pygame.display.flip()
pygame.quit()