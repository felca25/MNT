import numpy as np


import numpy as np

def main():
    players = ['X', 'O']
    game_running = True
    board = np.zeros(9)
    board_render = ['_', '_','_', '_', '_','_', ' ', ' ',' ']
    is_turn_x = True
    
    def check_winner():
        pass
    
    while game_running:
        for element in range(0, len(board)):
            if element in [2, 5, 8]:
                print(f'{board_render[element]}\n')

            else:
                print(f'{board_render[element]}' , end='|')
        
        print('------------------')
        
        if is_turn_x == 1:
            turn = 0
        else:
            turn = 1
            
        play = input(f'Vez do jogador {players[turn]} [1-9]\n')
        
        try:
            play = int(play)
            board_render[play - 1] = players[turn]
            is_turn_x = not is_turn_x
                
        except ValueError: 
            print('Type Error')
            game_running = False
            
        pass

if __name__ == "__main__":
    main()