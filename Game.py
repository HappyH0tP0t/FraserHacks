import pygame
import random
import time
import math

#Set up
pygame.init()
pygame.display.set_caption("It's Mathin' Time!")
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
 
        # initiate the properties
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

class BaseTarget(Block):
    def __init__(self, color, width, height, operatorType, operatorNumber):
        super().__init__(color, width, height)

        self.operatorType = operatorType
        self.operatorNumber = operatorNumber

# functions
def getBiasedTarget(current, goal):
    operators = ["+","-","*","/"]
    direction = math.copysign(1, goal - current)
    if direction > 0:
        operators += ["+", "+", "+", "*", "*", "*"]
    else:
        operators += ["-", "-", "-", "/", "/", "/"]
    return newTarget
    

##Main

#Variables

#List
all_sprites_list = pygame.sprite.Group()
target_list = pygame.sprite.Group()
scene_list = pygame.sprite.Group()

#Mouse position
last_frame_mouse_x, last_frame_mouse_y = pygame.mouse.get_pos()
mouse_x, mouse_y = pygame.mouse.get_pos()
last_frame_time = time.time()

#what the operator
operator = ["+","-","*","/"]

#scene number
scene = 1

#Colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

# Text
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Some Text', False, (0, 0, 0))

#images
intro_page = pygame.image.load('Start-screen-image.jpg')
intro_page = intro_page.convert()

# counters
goal_number = random.randint(0, 100)
current_number = random.randint(0, 100)
stopwatch = 0
game_time = 0

# This represents a button sprite
Button = Block(BLACK, 290,140)

# Set a location for the target sprite
Button.rect.x = 305
Button.rect.y = 290

# Add the target sprite to the list of objects
all_sprites_list.add(Button)
scene_list.add(Button)

#Target sprite set up
for i in range(5):
    # This represents a target sprite
    Target = BaseTarget(RED, 40, 40, operator[random.randint(0,3)], random.randint(1,5))

    # Set a random location for the target sprite
    Target.rect.x = random.randint(100, 800)
    Target.rect.y = random.randint(100, 500)
    for t in target_list:
        if Target.rect.collidepoint((t.rect.x, t.rect.y)):
            Target.rect.x = random.randint(100, 800)
            Target.rect.y = random.randint(100, 500)

    # Add the target sprite to the list of objects
    all_sprites_list.add(Target)
    target_list.add(Target)

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

    # keep an eye out for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for target in target_list:
                if (target.rect.collidepoint((mouse_x, mouse_y))):
                    print(str(target.operatorType)+ str(target.operatorNumber))
                    if target.operatorType == "+":
                        current_number += target.operatorNumber
                    if target.operatorType == "-":
                        current_number -= target.operatorNumber
                    if target.operatorType == "*":
                        current_number *= target.operatorNumber
                    if target.operatorType == "/":
                        current_number /= target.operatorNumber
                        current_number = int(current_number)
                    #REMOVING OLD TARGET
                    target.kill()
                    #CREATING NEW TARGET    
                    newTarget = BaseTarget(RED, 40, 40, operator[random.randint(0,3)], random.randint(1,5))
                    # Set a random location for the target sprite
                    newTarget.rect.x = random.randint(100, 800)
                    newTarget.rect.y = random.randint(100, 500)
                    for t in target_list:
                        if newTarget.rect.collidepoint((t.rect.x, t.rect.y)):
                            print("HEY")
                            newTarget.rect.x = random.randint(100, 800)
                            newTarget.rect.y = random.randint(100, 500)
                    newTarget = getBiasedTarget(current_number, goal_number)
                    # Add the target sprite to the list of objects
                    all_sprites_list.add(newTarget)
                    target_list.add(newTarget)
            for target in scene_list:
                if (target.rect.collidepoint(mouse_x, mouse_y)):
                    if scene == 1:
                        scene = 2
                        # sprite.update(color, BLACK)

                    else:
                        scene = 1
        #hack button which allows you to instally get to the goal number                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL:
                current_number = goal_number

    all_sprites_list.update()

    if scene == 1:
        screen.fill(WHITE)

        #pretty much just draws the targets rn
        scene_list.draw(screen)
        #summons the starting image
        screen.blit(intro_page, (0,0))


    elif scene == 2:
        Button.kill()
        # update screen (do this last)
        screen.fill(WHITE)

        #pretty much just draws the targets rn
        all_sprites_list.draw(screen)

        #gives it the operations
        for target in target_list:
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = my_font.render(target.operatorType + str(target.operatorNumber), False, BLACK)
            screen.blit(text_surface, (target.rect.x, target.rect.y))

        # draw the mouse
        pygame.draw.circle(screen, RED, (mouse_x, mouse_y), 10)

        # Increase the timer and check for wins
        stopwatch += delta_time
        if current_number == goal_number:
            current_number = random.randint(0, 100)
            goal_number = random.randint(0, 100)
            game_time = stopwatch
            stopwatch = 0
        
        # draw timers and scores
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        screen.blit(my_font.render("time: " + str(round(stopwatch)), False, (0, 0, 0)), (0, 0))
        screen.blit(my_font.render("current number: " + str(current_number), False, (0, 0, 0)), (0, 30))
        screen.blit(my_font.render("goal number: " + str(goal_number), False, (0, 0, 0)), (0, 60))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
