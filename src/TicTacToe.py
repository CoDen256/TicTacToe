import pygame
from tools import *
from screens.MainMenuScreen import MainMenuScreen


class TicTacToe:

    def __init__(self, w, h):
        self.size = self.w, self.h = w, h
        self.window = pygame.display.set_mode(self.size)
        self.current_screen = None
        self.mainloop = None

        pygame.init()

    def run(self, screen):
        self.current_screen = screen
        self.current_screen.create()

        self.mainloop = True
        self.update()

    def update(self):
        while self.mainloop:
            self.current_screen.handleInput()
            self.current_screen.update()
            self.current_screen.render()

    def change_screen(self, screen):
        self.quit()
        self.run(screen)

    def quit(self):
        self.mainloop = False
        quit_game()

game = TicTacToe(1080, 720)
game.run(MainMenuScreen(game))
