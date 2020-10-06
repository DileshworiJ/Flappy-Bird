import pygame, sys, random

def draw_base():
    screen.blit(base_surface, (base_x_pos,450))
    screen.blit(base_surface, (base_x_pos +288,450))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe =pipe_surface.get_rect(midtop= (350,random_pipe_pos))
    top_pipe =pipe_surface.get_rect(midbottom= (350,random_pipe_pos -150))
    return top_pipe, bottom_pipe
     

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2.5
    return pipes 

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >=512:   
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe,pipe)
 
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            print('collison detected')
    if bird_rect.top <= -50 or bird_rect.bottom >= 450:
        print('collison detected')

pygame.init()  #to initialize pygame library

screen = pygame.display.set_mode((288,512))  #method called display, set_mode takes width and height
clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load('assets/background-day.png').convert()           #adding background image #convert into the type that pygame feels easier, hepls ith consistency
base_surface = pygame.image.load('assets/base.png').convert()
base_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (50,200))

pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT                #TRIGGERED BY A TIMER USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)           #time in millisecond, 1.2sec
pipe_height = [200,300,400]
#scale image to screen dimension
#bg_surface = pygame.transform.scale2x(bg_surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()             #quit method
        if event.type == pygame.KEYDOWN:           #event codes are in uppercase
            if event.key ==pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6
        if event.type == SPAWNPIPE:         #checking for a condition when == is used
            pipe_list.extend(create_pipe())         #cannot append the tuple but should extend that list
            
    screen.blit(bg_surface,(0,0))
    
    bird_movement +=gravity
    bird_rect.centery += int(bird_movement)
    screen.blit(bird_surface,bird_rect)
    check_collision(pipe_list)

    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # screen.blit(bg_surface,(0,0))    #to display the image in the display screen
    base_x_pos -=1
    draw_base()
    if base_x_pos <= -288 :
        base_x_pos = 0

    pygame.display.update()
    clock.tick(120)  # framepersecond