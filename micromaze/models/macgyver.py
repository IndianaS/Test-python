#!/usr/bin/python3.7
# -*-coding:utf-8 -

import pygame
from constant import*



class MacGyver():

	def __init__(self, position, loot_item, move):
		#Current position MacGyver
		self.position = ()
		#Loot items
		self.loot_item = []
		#Move MacGyver
		self.move = move ()


	def position(display):
		pass
 



	def loot_item(self):
		pass



     #Move MacGyver
	def move(self):
		for event in pygame.event.get(pg.KEYDOWN):
			if event.key == pygame.K_UP:
				self.rect.move_ip(0, -settings.VELOCITY)
			elif event.key == pygame.K_DOWN:
				self.rect.move_ip(0, settings.VELOCITY)
			elif event.key == pygame.K_LEFT:
				self.rect.move_ip(-settings.VELOCITY, 0)
			elif event.key == pygame.K_RIGHT:
				self.rect.move_ip(settings.VELOCITY, 0)


    #Limit moves MacGyver
	def _limit_moves(self):
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > settings.WIDTH:
		    self.rect.right = settings.WIDTH
		if  self.rect.top < 0:
			 self.rect.top = 0
	    if self.rect.bottom > settings.HEIGHT:
	    	self.rect.bottom = settings.HEIGHT
 
		





        MacGyver = MG((), [], move)
	
    
    
