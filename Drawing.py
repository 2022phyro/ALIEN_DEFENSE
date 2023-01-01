import pygame
"""This module will contain the global settings like
stats, scores, screen setting, character settings, etc"""


class Background:
    """This class contains the tools needed to draw the background"""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images/Background.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

    def draw_background(self):
        """Draw the background"""
        self.screen.blit(self.image, self.rect)


class GameSettings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 690

