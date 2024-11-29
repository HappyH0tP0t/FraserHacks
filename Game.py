import pygame

#Set up
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

##Main

#Variables

#Color
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, red, (250, 250), 250)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
