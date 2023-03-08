import pygame as pg



windowRunning = True

def createWindow(title, width, height, backgroundColor=(0, 0, 0)):
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption(title)
    screen.fill(backgroundColor)

def createMainLoop(mainLoopFunc):
    pg.display.flip()

    while windowRunning:
        mainLoopFunc()

    