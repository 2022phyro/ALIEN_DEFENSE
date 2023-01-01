import sys
import pygame
"""This module will contain all the functions that will determine
more or less which part of the game should run"""

def check_events(soldier):
    """This checks the events, (keyboard or mouse input) and passes
    thses events to the appropriate classes"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            soldier.move_soldier(event)
        elif event.type == pygame.KEYUP:
            soldier.stop_soldier(event)

def update_screen(base_screen, soldier):
    """This draws the screen at any given moment"""
    pygame.display.flip()
    base_screen.draw_background()
    soldier.draw_soldier()