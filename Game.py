import pygame
import random

#Set up
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

##classes
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width,height):
        # Constructor. Pass in the color of the block, and its size.
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

##Main

#Variables
all_sprites_list = pygame.sprite.Group()

#Colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Target sprite set up
for i in range(5):
    # This represents a Bad sprite
    Target = Block(RED, 25,25)
 
    # Set a random location for the target sprite
    Target.rect.x = random.randint(100, 900)
    Target.rect.y = random.randint(100, 600)
 
    # Add the target sprite to the list of objects
    all_sprites_list.add(Target)

# Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255, 255, 255))

    all_sprites_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
