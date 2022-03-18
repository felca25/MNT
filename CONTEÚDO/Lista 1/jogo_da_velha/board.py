import numpy as np

class Board():
    def __init__(self) -> None:
        self.board = np.zeros(9)
        self.board_x = []
        self.board_o = []
        self.turn_x = True
        
    def initialize_board():
        print('Jogo da velha')
        print('--------------')    
    def get_selection():
        play = input('Please select a square to play')