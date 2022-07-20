import pygame
import colors

cellSize = 50
gridWidth = 10
gridHeight = 10

width = gridWidth*cellSize  #ширина
height = gridHeight*cellSize #высота
window_caption = ""
FPS = 60
background = colors.grey

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(window_caption)
clock = pygame.time.Clock()
screen.fill(background)
pygame.display.update()

game = True

while game :
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                game = False
    screen.fill(background)
    
    for i in range(gridWidth):
        pygame.draw.line(screen, (0,0,0), (i*cellSize, 0), (i*cellSize, height))
    for i in range(gridHeight):
        pygame.draw.line(screen, (0,0,0), (0, i*cellSize), (width, i*cellSize))

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()