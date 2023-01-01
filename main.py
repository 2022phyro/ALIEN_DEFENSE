import pygame
from Drawing import Background, GameSettings
from Characters import Soldier
import Game_functions as g
"""This module will run the game"""

def run():
    """This function is mothing but a framework of the other
    functions and classes pu together"""
    pygame.init()
    gme = GameSettings()
    screen = pygame.display.set_mode((gme.screen_width, gme.screen_height))
    pygame.display.set_caption("Alien Defense", "AD")
    base_screen = Background(screen)
    soldier = Soldier(screen, gme)
    while True:

        g.check_events(soldier)
        soldier.update()
        g.update_screen(base_screen, soldier)

run()