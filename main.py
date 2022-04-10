import pygame
import linecache
from Code.Fps.FPS import FPSS
from Code.Mouse import Mouse
pygame.init()

Red = [255, 0, 0]
Purp = [255, 0, 222]
Blue = [85, 0, 255]
LBlue = [0, 205, 255]
Green = [0, 255, 111]

pygame.mouse.set_visible(0)

class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.Font = pygame.font.Font("APOLLO.otf",20)
        self.FPS = self.Font.render(str(round(self.clock.get_fps())),True,Red)
    def Render(self,screen):
        self.FPS = self.Font.render(str(round(self.clock.get_fps())),True,Red)
        screen.blit(self.FPS,(40,0))

fps = FPS()


ScreenRes_x = linecache.getline(r"Config.txt",6)
ScreenRes_y = linecache.getline(r"Config.txt",7)
#Grabbing the screen res from config
screen = pygame.display.set_mode((int(ScreenRes_x),int(ScreenRes_y)))


Running = Truee

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            from sys import exit
            exit()
            Running = False
    if Running == False:
        from sys import exit
        exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        from sys import exit
        exit()
        Running == False

    white = [255,255,255]
    screen.fill(white)
    fps.Render(screen)
    FPSS().fps()
    Mouse().mouse()

    pygame.display.update()
    FramesASecond = linecache.getline(r"Config.txt",2)
    fps.clock.tick(int(FramesASecond))
