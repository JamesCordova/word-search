# We are gonna create a tower defense game with binaries 
# and buses in cmoputers arquitecture, the game should have
# the following:
# - Words, that means bytes that are gonna move through a 
#   path defined by points in screen to follow, once reach 
#   the last point it causes bad puntuation or less score.
#   the words should be displayed 
#   (the points are defined by the buses)
# - Unit, this class should be the core of something that 
#   receives damage when words reach last point to follow
# - Bus, there will be buses to move the words, and connect
#   all units
# Now the game should start with receiving word through the
# buses and we need to be careful of accepting words in red
# that words don't mean to be accepted, so if certain amount
# of bad words reach the unit means game over.
import pygame
import random

# Class word of random bits to generate and "bad" property
class Word(pygame.sprite.Sprite):
    def __init__(self, bad = False):
        super().__init__()
        self.bits_quantity = 8
        self.bits = []
        self.bad = bad

        self.generate_bits()



    def generate_bits(self):
        for bit in range(self.bits_quantity):
            self.bits.append(random.randint(0, 1))