import pygame
import sys
from pygame import display
from pygame.constants import QUIT

pygame.init()
class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image=pygame.image.load("Sketch006.png")
        self.pos=(300,300)
    def draw():
        screen.blit(image,pos)
    
screen=pygame.display.set_mode((800,600))
player_x=300
player_y=300
bg_color = (230, 230, 230)
def player():
    
    
pygame.display.set_caption("ah ahhh ahaa")

icon=pygame.image.load("Sketch004.png")

pygame.display.set_icon(icon)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        screen.fill(bg_color)
        player()
      
        
        pygame.display.update()
