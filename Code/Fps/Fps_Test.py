import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))

Red = [255, 0, 0]
Purp = [255, 0, 222]
Blue = [85, 0, 255]
LBlue = [0, 205, 255]
Green = [0, 255, 111]
Test = pygame.draw.rect(screen, Red, (screen.get_height()/2, screen.get_width()/2, 400, 200))

Test_Image = pygame.image.load("Code/Fps/Black_PSL.png").convert_alpha()
Test_ImageR = pygame.transform.smoothscale(Test_Image,(175,100)).convert_alpha()
TestR = Test_ImageR.get_rect(topleft=(screen.get_width()/2, screen.get_height()/2))
Test_ImageR2 = pygame.transform.smoothscale(Test_Image,(275,200)).convert_alpha()

class FpsTest(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.AnimationP = True
        self.sprites = []
        self.sprites.append(Test_ImageR)
        self.sprites.append(Test_ImageR2)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [screen.get_width()/2, screen.get_height()/2]

        pos = pygame.mouse.get_pos()


    def update(self):
        if self.AnimationP == True:
            self.current_sprite += 0.3

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

ButtonAnim = pygame.sprite.Group()
BA = FpsTest(200,200)
ButtonAnim.add(BA)

# Fps test is a go
class FPSTIAG:
    def FPSTest(self):
        AnimIP = False
        pos = pygame.mouse.get_pos()
        screen.blit(Test_ImageR,TestR)
        if pygame.mouse.get_pressed()==(1,0,0):
            if Test.collidepoint(pos):
                AnimIP == True


        ButtonAnim.draw(screen)
        ButtonAnim.update()
