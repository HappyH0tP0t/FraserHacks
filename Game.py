import pygame
import time

#Set up
pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()
running = True

##Main

#Variables
lastFrameMouseX, lastFrameMouseY = pygame.mouse.get_pos()
mouseX, mouseY = pygame.mouse.get_pos()
lastFrameTime = time.time()

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
    pygame.display.flip()

pygame.quit()
