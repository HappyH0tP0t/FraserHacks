import pygame
import random
import time

#Set up
pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()
running = True
pygame.font.init() 

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
lastFrameMouseX, lastFrameMouseY = pygame.mouse.get_pos()
mouseX, mouseY = pygame.mouse.get_pos()
lastFrameTime = time.time()
## Text
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Some Text', False, (0, 0, 0))

#The target things
targets = [
    {
        "positionX": 0,
        "positionY": 0,
        "text": "5"
    }
]

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
    # calculate deltatime
    currentTime = time.time()
    deltaTime = currentTime - lastFrameTime
    lastFrameTime = currentTime
    # calculate mouse deltas
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseDeltaX, mouseDeltaY = mouseX - lastFrameMouseX, mouseY - lastFrameMouseY
    lastFrameMouseX, lastFrameMouseY = mouseX, mouseY
    
    # debbug
    # print(deltaTime)

    # keep an eye out for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update screen (do this last)     
    screen.fill((255, 255, 255))

    all_sprites_list.draw(screen)



    pygame.draw.circle(screen, RED, (mouseX, mouseY), 10)
    screen.blit(text_surface, (mouseX, mouseY))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
