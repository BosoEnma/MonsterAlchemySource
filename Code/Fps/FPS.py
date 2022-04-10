import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))

class FPSS:
    def fps(self):
        Red = [255, 0, 0]
        Purp = [255, 0, 222]
        Blue = [85, 0, 255]
        LBlue = [0, 205, 255]
        Green = [0, 255, 111]
        Font = pygame.font.Font("APOLLO.otf", 20)
        FPS = Font.render("Fps: ", True, Red)
        screen.blit(FPS, (0,0))