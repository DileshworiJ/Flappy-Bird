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
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 450:
            return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement *3, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (50, bird_rect.centery))
    return new_bird,new_bird_rect
    

pygame.init()  #to initialize pygame library

screen = pygame.display.set_mode((288,512))  #method called display, set_mode takes width and height
clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0
game_active = True

bg_surface = pygame.image.load('assets/background-day.png').convert()           #adding background image #convert into the type that pygame feels easier, hepls ith consistency
base_surface = pygame.image.load('assets/base.png').convert()
base_x_pos = 0

# bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
# bird_rect = bird_surface.get_rect(center = (50,200))

bird_downflap = pygame.image.load('assets/bluebird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('assets/bluebird-upflap.png').convert_alpha() 
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (50,256))


BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)


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
            if event.key ==pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6
            if event.key ==pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (50, 256)
                bird_movement = 0

        if event.type == SPAWNPIPE:         #checking for a condition when == is used
            pipe_list.extend(create_pipe())         #cannot append the tuple but should extend that list
        
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
        else:
            bird_index = 0

        bird_surface,bird_rect = bird_animation()    



    screen.blit(bg_surface,(0,0))

    if game_active:
        bird_movement += gravity         
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += int(bird_movement)
        screen.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

    # screen.blit(bg_surface,(0,0))    #to display the image in the display screen
    base_x_pos -=1
    draw_base()
    if base_x_pos <= -288 :
        base_x_pos = 0
    pygame.display.update()
    clock.tick(120)  # framepersecond