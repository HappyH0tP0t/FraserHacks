import pygame
import random
import time
import math

#Set up
pygame.init()
pygame.display.set_caption("It's MATHin' Time!")
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
    if difficulty == "hard":
        direction *= -1
        operators += ["^", "√"]
    if direction > 0:
        operators += ["+", "+", "+", "*", "*", "*"]
    else:
        operators += ["-", "-", "-", "/", "/", "/"]
    newTarget = BaseTarget(WHITE, target_hitbox_length, target_hitbox_length, operators[random.randint(0,len(operators) - 1)], random.randint(1,5))

    # Set a random location for the target sprite
    newTarget.rect.x = random.randint(100, 800)
    newTarget.rect.y = random.randint(100, 450)
    for sprite in target_list:
        if pygame.sprite.collide_rect(sprite, newTarget):
            newTarget.rect.x = random.randint(100, 800)
            newTarget.rect.y = random.randint(100, 450)

    return newTarget
    

##Main
#Colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

#Variables

credits = False

#play button dimensions
play_button_x = 315
play_button_y = 245
play_button_width = 290
play_button_length = 140

target_hitbox_length = 75

#List
all_sprites_list = pygame.sprite.Group()
target_list = pygame.sprite.Group()
scene_list = pygame.sprite.Group()
difficulty_list = pygame.sprite.Group()

# counters
goal_number = random.randint(0, 100)
current_number = random.randint(0, 100)
stopwatch = 0
game_time = 0
difficulty = "easy"

#scene number
scene = 1

#Mouse position
last_frame_mouse_x, last_frame_mouse_y = pygame.mouse.get_pos()
mouse_x, mouse_y = pygame.mouse.get_pos()
last_frame_time = time.time()

#what the operator
operator = ["+","-","*","/"]

#scene number
scene = 1

# Text
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Some Text', False, BLACK)
final_time = my_font.render('Some Text', False, BLACK)

#images
intro_page = pygame.image.load('Start-screen-image.jpg')
intro_page = pygame.transform.scale(intro_page,(960, 540))
intro_page = intro_page.convert()

edging_page = pygame.image.load('ending-screen.jpg')
edging_page = pygame.transform.scale(edging_page,(960, 540))
edging_page = edging_page.convert()

credits_image = pygame.image.load('credits!.jpg')
#credits = pygame.transform.scale(credits,(960, 540))
credits_image = credits_image.convert()

# counters
goal_number = random.randint(0, 100)
current_number = random.randint(0, 100)
stopwatch = 0
game_time = 0
difficulty = "easy"

#Object creation
# Create Buttons
PlayButton = Block(WHITE, play_button_width,play_button_length)
DifficultyButton = Block(GREEN, 50, 50)

# Set a location for the target sprite
PlayButton.rect.x = play_button_x
PlayButton.rect.y = play_button_y
DifficultyButton.rect.x = 120
DifficultyButton.rect.y = 480

# Add the target sprite to the list of objects
all_sprites_list.add(PlayButton)
scene_list.add(PlayButton)
all_sprites_list.add(DifficultyButton)
difficulty_list.add(DifficultyButton)

#Target sprite set up
for i in range(5):
    # This represents a target sprite
    Target = BaseTarget(WHITE, target_hitbox_length, target_hitbox_length, operator[random.randint(0,3)], random.randint(1,5))

    # Set a random location for the target sprite
    Target.rect.x = random.randint(100, 800)
    Target.rect.y = random.randint(100, 450)
    for t in target_list:
        if pygame.sprite.collide_rect(t, Target):
            Target.rect.x = random.randint(100, 800)
            Target.rect.y = random.randint(100, 450)

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
            if scene == 1:
                if mouse_x >= play_button_x and mouse_x <= play_button_x+play_button_width and mouse_y >= play_button_y+125 and mouse_y <= play_button_y+play_button_length+125 and credits == False:
                    credits = True
                else:
                    credits = False

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
                    if target.operatorType == "√":
                        if current_number != 0:
                            current_number = math.sqrt(current_number)
                    if target.operatorType == "^":
                        current_number = math.pow(current_number, target.operatorNumber)
                    current_number = int(current_number)
                    current_number = max(current_number, 0)

                    #REMOVING OLD TARGET
                    target.kill()

                    #CREATING NEW TARGET    
                    newTarget = getBiasedTarget(current_number, goal_number)
                    
                    newTarget = getBiasedTarget(current_number, goal_number)
                    
                    # Add the target sprite to the list of objects
                    all_sprites_list.add(newTarget)
                    target_list.add(newTarget)
            for sprite in scene_list:
                if (sprite.rect.collidepoint(mouse_x, mouse_y)):
                    if scene == 1:
                        scene = 2
                    else:
                        scene = 1
            for sprite in difficulty_list:
                if (sprite.rect.collidepoint(mouse_x, mouse_y)):
                    if difficulty == "easy":
                        difficulty = "hard"
                    else:
                        difficulty = "easy"
                    sprite.kill()
                    DifficultyButton = Block(GREEN if difficulty == "easy" else RED, 50, 50)
                    DifficultyButton.rect.x = 120
                    DifficultyButton.rect.y = 480
                    all_sprites_list.add(DifficultyButton)
                    difficulty_list.add(DifficultyButton)


        #hack button which allows you to instally get to the goal number                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL and scene == 2:
                current_number = goal_number

    all_sprites_list.update()

    if scene == 1:
        screen.fill(WHITE)

        #pretty much just draws the targets rn
        scene_list.draw(screen)

        #summons the starting image
        screen.blit(intro_page, (0,0))

        difficulty_list.draw(screen)

        if credits == True:
            screen.blit(credits_image, (150,150))


    elif scene == 2:
        PlayButton.kill()
        DifficultyButton.kill() 
        scene_list.remove(PlayButton)
        # update screen (do this last)
        screen.fill(WHITE)

        #pretty much just draws the targets rn
        all_sprites_list.draw(screen)
        for target in target_list:
            target_circle = pygame.draw.circle(screen, RED, target.rect.center, 40)

            #gives it the operations
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = my_font.render(target.operatorType + (str(target.operatorNumber) if target.operatorType != "√" else ""), False, BLACK)
            screen.blit(text_surface, (target_circle.centerx - 20, target_circle.centery - 20))

        # draw the mouse
        pygame.draw.circle(screen, RED, (mouse_x, mouse_y), 10)

        # Increase the timer
        stopwatch += delta_time
        #if your current number is the same as the goal_number you win
        if current_number == goal_number:
            current_number = random.randint(0, 100)
            goal_number = random.randint(0, 100)
            game_time = stopwatch
            stopwatch = 0
            scene = 3

            #adding back the playbutton and the difficulty button
            scene_list.add(PlayButton)
            difficulty_list.add(DifficultyButton)

            #rendering the text for the final time
            final_time_text = my_font.render("Your final time is:", False, WHITE)   
            final_time = my_font.render(str(round(game_time,3)), False, WHITE)                
        
        # draw timers and scores
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        screen.blit(my_font.render("time: " + str(round(stopwatch * 1000) / 1000), False, BLACK), (0, 0))
        screen.blit(my_font.render("current number: " + str(current_number), False, BLACK), (0, 30))
        screen.blit(my_font.render("goal number: " + str(goal_number), False, BLACK), (0, 60))

    elif scene == 3:

        #screen background fill
        screen.fill(BLACK)
       
        #drawing the button
        scene_list.draw(screen)

        #bliting the end screen
        screen.blit(edging_page, (0,0))

        #bliting the final time
        screen.blit(final_time_text, (40,300))
        screen.blit(final_time, (120, 350))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
