import pygame as pygame

from config import settings

class MapSprite(pg.sprite.Sprite):

	def __init__(self):
		self.image = pg.image.load(settings.BACKGROUND).convert()
		self.rect = self.image.get_rect()
