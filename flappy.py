import pygame, sys
def draw_base():
    screen.blit(base_surface, (base_x_pos,450))
    screen.blit(base_surface, (base_x_pos +288,450))


pygame.init()  #to initialize pygame library

screen = pygame.display.set_mode((288,512))  #method called display, set_mode takes width and height
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png').convert()           #adding background image #convert into the type that pygame feels easier, hepls ith consistency
base_surface = pygame.image.load('assets/base.png').convert()
base_x_pos = 0
#scale image to screen dimension
#bg_surface = pygame.transform.scale2x(bg_surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()             #quit method
    screen.blit(bg_surface,(0,0))    #to display the image in the display screen
    base_x_pos -=1
    draw_base()
    if base_x_pos <= -288 :
        base_x_pos = 0

    pygame.display.update()
    clock.tick(120)  # framepersecond