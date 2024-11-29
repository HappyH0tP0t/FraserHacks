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
    def __init__(self, color, width,height, operatorType, operatorNumber):
        # Constructor. Pass in the color of the block, and its size.
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # initiate the properties
        self.operatorType = operatorType
        self.operatorNumber = operatorNumber
        self.color = color
        self.width = width
        self.height = height

        # Create an image of the block, and fill it with a color
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
    def updateAppearance(self):
        # Create an image of the block, and fill it with a color
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(self.color)

        # create text
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(self.operatorType + str(self.operatorNumber), False, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x, self.rect.y))

        #Game content setup
def start_generate_values():
    goal_value = randint(1, 101) #the goal the player tries to reach
    starting_value = randint(1,11) #the number the player starts with

##Main


#Variables
all_sprites_list = pygame.sprite.Group()

last_frame_mouse_x, last_frame_mouse_y = pygame.mouse.get_pos()
mouse_x, mouse_y = pygame.mouse.get_pos()
last_frame_time = time.time()

## Text
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Some Text', False, (0, 0, 0))

#Colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Target sprite set up
for i in range(5):
    # This represents a Bad sprite
    Target = Block(RED, 25,25, "*", 4)
 
    # Set a random location for the target sprite
    Target.rect.x = random.randint(100, 800)
    Target.rect.y = random.randint(100, 500)
 
    # Add the target sprite to the list of objects
    all_sprites_list.add(Target)

# Loop
while running:
    # calculate deltatime
    current_time = time.time()
    delta_time = current_time - last_frame_time
    last_frame_time = current_time

    # calculate mouse deltas
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_delta_x, mouse_delta_y = mouse_x - last_frame_mouse_x, mouse_y - last_frame_mouse_y
    last_frame_mouse_x, last_frame_mouse_y = mouse_x, mouse_y
    
    # debbug
    # print(deltaTime)

    # keep an eye out for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in all_sprites_list:
                if (sprite.rect.collidepoint((mouse_x, mouse_y))):
                    print(str(sprite.operatorType)+ str(sprite.operatorNumber))
                    sprite.kill()
    for sprite in all_sprites_list:
        sprite.updateAppearance()
    
    # update screen (do this last)     
    screen.fill((255, 255, 255))

    all_sprites_list.draw(screen)

    pygame.draw.circle(screen, RED, (mouse_x, mouse_y), 10)
    screen.blit(text_surface, (mouse_x, mouse_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
