import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Prueba de Pygame")

screen.fill((255, 255, 255))

rect2 = pygame.Rect(200, 200, 100, 100)

def cambio():
    screen = pygame.display.set_mode((800, 600))
    #screen.fill((0, 0, 0))  
    #pygame.draw.rect(screen, (0, 255, 0), rect2)

rect = pygame.Rect(100, 100, 100, 100)
pygame.draw.rect(screen, (255, 0, 0), rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            #change surface
            cambio()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #detect click on rect2
            if rect2.collidepoint(event.pos):
                print("Click on rect2")
    
    pygame.display.update()

