import pygame
pygame.init()
from Code.Splash.splash import S
image = pygame.image.load("Assets/Splash/Grass_1.png").convert_alpha()
imagerect =  image.get_rect(topleft=(1280,720))
class Link:
    def __init__(self):
        self.Princess = S().Princess


