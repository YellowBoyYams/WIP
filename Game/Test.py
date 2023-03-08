import Scrappy.main as mn
import pygame


def mainLoop():
    for event in pygame.event.get():
        
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                mn.windowRunning = False

mn.createWindow("Testing", 300, 400)

mn.createMainLoop(mainLoop)