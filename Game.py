import pygame
import time

#Set up
pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()
running = True

##Main
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)


#Variables
lastFrameMouseX, lastFrameMouseY = pygame.mouse.get_pos()
mouseX, mouseY = pygame.mouse.get_pos()
lastFrameTime = time.time()
text_surface = my_font.render('Some Text', False, (0, 0, 0))

#Color
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Loop
while running:
    # calculate deltatime
    currentTime = time.time()
    deltaTime = currentTime - lastFrameTime
    lastFrameTime = currentTime
    # calculate mouse deltas
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseDeltaX, mouseDeltaY = mouseX - lastFrameMouseX, mouseY - lastFrameMouseY
    lastFrameMouseX, lastFrameMouseY = mouseX, mouseY
    
    # debbug
    print(deltaTime)

    # keep an eye out for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update screen (do this last)
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, red, (mouseX, mouseY), 10)
    screen.blit(text_surface, (mouseX, mouseY))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
