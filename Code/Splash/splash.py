import linecache

import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))

Moon = pygame.image.load("Assets/Splash/Moon.png").convert_alpha()
BGFog = pygame.image.load("Assets/Splash/BG_Fog.png").convert_alpha()
PrincessA = pygame.image.load("Assets/Splash/Princess.png").convert_alpha()
PrincessRect = PrincessA.get_rect(topleft=(0,0))
Ground_Layer_1A = pygame.image.load("Assets/Splash/Ground_1.png").convert_alpha()
Ground_Layer_2 = pygame.image.load("Assets/Splash/Ground_2.png").convert_alpha()
Ground_Layer_3 = pygame.image.load("Assets/Splash/Ground_3.png").convert_alpha()
Beam_O_Light = pygame.image.load("Assets/Splash/Light_Beam.png").convert_alpha()
Una_Casa = pygame.image.load("Assets/Splash/Far_D_Casa.png").convert_alpha()
Blossom = pygame.image.load("Assets/Splash/Blossom_Pedal.png").convert_alpha()
BlossomR = pygame.transform.smoothscale(Blossom,(50,56)).convert_alpha()


class S:
    def __init__(self):
        grey = [45,45,45]
        screen.fill(grey)
        self.Fog = screen.blit(BGFog,(0,0))
        self.Moon = screen.blit(Moon,(0,0))
        self.BeamOfLight = screen.blit(Beam_O_Light,(0,0))
        self.Casa = screen.blit(Una_Casa,(0,0))
        self.Grounf_3 = screen.blit(Ground_Layer_3, (0, 0))
        self.Grounf_2 = screen.blit(Ground_Layer_2,(0,0))
        self.Ground_1 = screen.blit(Ground_Layer_1A, (0, 0))
        self.Princess = screen.blit(PrincessA,PrincessRect)
        self.Pedal = screen.blit(BlossomR,(0,0))

