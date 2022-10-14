'''Run this to start Rock Paper Scissors Game.'''
# Student Name: Chen Chen
# Student Number: S360496
import sys
from game import Game

Game.game_start(Game)
while True:
    play_again = input("Restart the game (Y/N): ")
    if play_again in ("Y", "y"):
        Game.game_start(Game)
    if play_again in ("N", "n"):
        sys.exit()
