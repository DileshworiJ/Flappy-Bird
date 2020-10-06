import pygame, sys

def draw_base():
    screen.blit(base_surface, (base_x_pos,450))
    screen.blit(base_surface, (base_x_pos +288,450))

def create_pipe():
    new_pipe =pipe_surface.get_rect(midtop= (350,256))
    return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2.5
    return pipes 

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)

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
            pipe_list.append(create_pipe())
            print(pipe_list)

    screen.blit(bg_surface,(0,0))
    
    bird_movement +=gravity
    bird_rect.centery += int(bird_movement)
    screen.blit(bird_surface,bird_rect)

    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # screen.blit(bg_surface,(0,0))    #to display the image in the display screen
    base_x_pos -=1
    draw_base()
    if base_x_pos <= -288 :
        base_x_pos = 0

    pygame.display.update()
    clock.tick(120)  # framepersecond