import pygame
"""This module contains the characters for the game
It holds the soldier and the aliens which will come soon after"""
class Soldier:
    """This is our playable character who will save the world from all aliens"""
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.gme = game_settings
        self.image = pygame.image.load("Images/Standing.png")
        self.image.set_colorkey((3, 4, 8))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom
        #Initializing constant variables as we change pictures
        self.o_a = self.rect.left
        self.o_b = self.rect.bottom
        #Initializing movement flags
        self.left = False
        self.move_right = False
        self.up = False
        self.down = False
    def move_soldier(self, event):
        """Ensure continous movement. once a key is pressed, the falg will be true
        and movement will occur"""
        if event.key == pygame.K_RIGHT:
            self.move_right = True
        if event.key == pygame.K_DOWN:
            self.down = True
        if event.key == pygame.K_LEFT:
            self.left = True

    def stop_soldier(self, event):
        """Stop movement"""
        if event.key == pygame.K_RIGHT:
            self.move_right = False
        if event.key == pygame.K_DOWN:
            self.down = False
        if event.key == pygame.K_LEFT:
            self.left = False

    def update(self):
        """This method changes the pictures and the rect positions according to
        the movement involved"""
        if self.down:
            self.init_movement_picture("Bending")
        else:
            self.init_movement_picture("Standing")
        if self.move_right:
            self.o_a += 2
            self.rect.left = self.o_a
        if self.left:
            self.o_a -= 2
            self.rect.left = self.o_a
    def draw_soldier(self):
        """This draws the soldier onto the screen"""
        self.screen.blit(self.image, self.rect)

    def init_movement_picture(self, filename):
        """This function switches the pictures and intializes them"""
        self.image = pygame.image.load("Images/" + filename + ".png")
        self.image.set_colorkey((3, 4, 8))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.left = self.o_a
        self.rect.bottom = self.o_b