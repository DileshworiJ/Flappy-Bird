import pygame, sys

pygame.init()  #to initialize pygame library

screen = pygame.display.set_mode((288,512))  #method called display, set_mode takes width and height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()              #quit method
    pygame.display.update()