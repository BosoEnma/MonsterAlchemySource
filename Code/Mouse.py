import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
class Mouse:
    def mouse(self):
        Mouse_Pointer = pygame.image.load("Mouse_Pointer.png").convert_alpha()
        RealMouse = pygame.transform.smoothscale(Mouse_Pointer, (25, 25))
        Mouse_PointerRage = pygame.image.load("Mouse_Pointer_RAGE.png").convert_alpha()
        RealMouseRage = pygame.transform.smoothscale(Mouse_PointerRage, (25, 25))

        screen.blit(RealMouse, (pygame.mouse.get_pos()))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pos = pygame.mouse.get_pos()
            screen.blit(RealMouseRage, pos)