import pygame.key
from Code.Link import bridge
import linecache

class All_Lie_Here:
    def ALH(self):
        #bridge().FPSTest
        keys = pygame.key.get_pressed()
        Splash = True
        Splash2 = False
        if keys[pygame.K_SPACE]:
            Splash = False
            Splash2 = True

        if Splash == True:
            bridge().Splash_Link
            Splash2 = False

        if Splash2 == True:
            bridge().Splash2()
    def Game(self):
        All_Lie_Here().ALH()