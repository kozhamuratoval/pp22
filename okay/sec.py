from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
surface = pygame.display.set_mode((600, 400))

def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
def start_the_game():
    pass
def level_menu():
    mainmenu._open(level)

mainmenu = pygame_menu.Menu("Welcome", 600, 400, theme = themes.THEME_SOLARIZED)
mainmenu.add.text_input("Name: ", default = 'username', maxchar = 20)
mainmenu.add.button("Play", start_the_game)
mainmenu.add.button("Levels", level_menu)
mainmenu.add.button("Quit", pygame_menu.events.EXIT)

level = pygame_menu.Menu("Select a Difficulty", 600, 400, theme = themes.THEME_BLUE)
level.add.selector("Difficulty:", [("Hard", 1), ("Easy", 2)], onchange = set_difficulty)

#mainmenu.mainloop(surface)
