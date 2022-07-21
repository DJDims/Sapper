import pygame
import random
import cell

cellSize = 50
gridWidth = 10
gridHeight = 10

width = gridWidth*cellSize  #ширина
height = gridHeight*cellSize #высота
window_caption = "Сапер"
FPS = 60
background = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(window_caption)
clock = pygame.time.Clock()
screen.fill(background)
pygame.display.update()

done = True
game = True

cells = []

x = 0
y = 0
for i in range(1, gridWidth*gridHeight+1):
    mine = False
    if random.randint(0, 100)%5 == 0:
        mine = True

    cells.append(cell.cell(i, x, y, mine, False))

    x += 1
    if x%10 == 0 :
        x = 0
        y+=1

while done :
    clickedImage = None
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                done = False
        elif i.type == pygame.MOUSEBUTTONUP and game == True:
            print(i.button)
            mousePos = pygame.mouse.get_pos()
            for j in cells:
                if j.x*cellSize < mousePos[0] < j.x*cellSize+cellSize and j.y*cellSize < mousePos[1] < j.y*cellSize+cellSize:
                    clickedImage = j
                    if i.button == 1:
                        clickedImage.countMines(cells)
                    elif i.button == 3:
                        clickedImage.flag = True
            
    screen.fill(background)
    
    for i in cells:
        screen.blit(pygame.image.load(i.image), (i.x*cellSize, i.y*cellSize))

    if clickedImage != None and clickedImage.mine == True and clickedImage.flag == False:
        game = False
        for i in cells:
            if i.mine == True:
                i.image = "Images/mine.png"
            screen.blit(pygame.image.load(i.image), (i.x*cellSize, i.y*cellSize))
    elif clickedImage != None and clickedImage.mine == False and clickedImage.flag == False:
        clickedImage.image = f"Images/mines_{clickedImage.aroundMines}.png"
        screen.blit(pygame.image.load(clickedImage.image), (clickedImage.x*cellSize, clickedImage.y*cellSize))
    elif clickedImage != None and clickedImage.flag == True:
        clickedImage.image = "Images/flag.png"
        screen.blit(pygame.image.load(clickedImage.image), (clickedImage.x*cellSize, clickedImage.y*cellSize))

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()