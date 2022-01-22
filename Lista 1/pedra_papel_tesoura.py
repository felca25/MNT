import random
"""
JANEIRO DE 2022

FELIPE CARVALHO ANDRADE - 17/0162010

UNIVERSIDADE DE BRASÍLIA
FACULDADE DE TECNOLOGIA
DEPARTAMENTO DE ENGENHARIA MECÂNICA
MÉTODOS NUMÉRICOS EM TERMOFLUIDOS
"""

'''
Este é um jogo de pedra papel e tesoura de melhor de 5 (geralmente são 5 partidas se ambos ganharem consecutivamente), 
mas ganha quem ganhar 3 partidas primeiro.

Para jogar digite uma das três opções (rock, paper, scissors), e espere a resposta do computador.

Existem dois modos: justo (computador pode ganhar) e injusto (computador sempre ganha)
'''

class Game:
    """
    Uma classe que funciona como um jogo de pedra, papel e tesoura
    ...
    Atributos
    ---------
    user_input: int
        o valor da jogada do usuário (pedra[0], papel[1], tesoura[2])
    computer: int
        o valor da jogada do computador (pedra[0], papel[1], tesoura[2])
    computer_play: string
        a jogada do computador
    computer_wins: int
        quantas partidas o computador venceu
    user_wins: int
        quantas partidas o usuário venceu
    round: int
        qual a partida atual
    continue_game: bool
        variável booleana que define para o loop while se o jogo deve continuar ou parar
        
    Methods
    -------
    getUserInput()
        pega a jogada do usuário, converte em números e salva em self.user_input
    comp_play(computer_input: int)
        converte as jogadas numéricas do computador em palavras de forma a facilitar a compreensão do usuário
    fair_computer()
        gera uma jogada aleatória para o computador
    unfair_computer
        gera uma jogada que necessariamente vai ganhar do usuário
    calculate_winner(user_input: int, computer_input: int)
        calcula o ganhador de uma partida
    register_match_results(result: str)
        registra o resultado da partida em self.user_wins ou self.computer_wins
    check_for_winners()
        checa o número de vitórias para encontrar um vencedor e mudar o valor de self.continue_game para parar o jogo
    game_result()
        printa o resultado do jogo
    reset_game()
        reseta o jogo (reinicia o valor das variáveis)
    fair_game()
        função que contém o jogo justo
    unfair_game()
        função que contém o jogo injusto
        
    Returns:
        None : essa classe não retorna nada
    """
    def __init__(self):
        # primeiro vamos iniciar a classe com valores impossíveis de serem inputados, para que se ocorrer um erro saibamos de onde ele vem
        self.user_input = 3;
        self.computer = 4;
        self.computer_play = ""
        self.computer_wins = 0
        self.user_wins = 0
        self.round = 0
        self.continue_game = True
        pass
    
    def getUserInput(self):
        # agora vamos pegar o input do usuário e vamos tratar esse input para obter valores numéricos
        print('Round %s. Enter "q" to exit the game.'% self.round)
        print('----------------')
        user_input = input('Rock, Paper, Scissors \n').lower()
        
        if user_input == 'rock':
            self.user_input = 0
        elif user_input == 'paper':
            self.user_input = 1
        elif user_input == 'scissors':
            self.user_input = 2
        else:
            # novamente vamos colocar um valor impossível de ser inputado para controle de erro
            self.user_input = 10
            # retornando 0, 1 desta forma podemos saber se a função rodou de forma correta ou não
            return 0
        return 1
    
    def comp_play(self, computer_input):
        # aqui vamos converter os inputs numéricos do computador em uma jogada para o usuário
        if computer_input == 0 or computer_input == 3:
            self.computer_play = 'rock'
        elif computer_input == 1:
            self.computer_play = 'paper'
        elif computer_input == 2:
            self.computer_play = 'scissors'
        else:
            self.computer_play = 'play out of range'
    
    def fair_computer(self):
        # gerando um número aleatório em [0,1,2,3] "mas não existe só 3 inputs possíveis? Porque temos 4 indices?"
        # você entenderá quando fomos ver como o ganhador é calculado
        self.computer = random.randint(0,3)
        #convertendo o número em jogada
        self.comp_play(self.computer)
        print(self.computer_play)
        
    def unfair_computer(self):
        # aqui só colocamos que a jogada que o computador fará será a jogada que ganha do usuário
        self.computer = self.user_input + 1
        # convertendo o número em jogada
        self.comp_play(self.computer)
        print(self.computer_play)
        
    
    def calculate_winner(self, user_input, computer_input):
        # Como calcular o vencedor
        # temos as seguintes jogadas que formam um ciclo 
        #  ... -> pedra [0] -> papel[1] -> tesoura[2] -> pedra[3] ...
        # como estamos usando números ao invés de palavras, podemos dizer que o computador ganha se o seu input for
        # igual a o input do usuário + 1, desta forma:
        if user_input == computer_input or computer_input - 3 == user_input:
            # existem duas formas de ter um empate: se a jogada do usuário for a mesma que a do computador e se a 
            # jogada do computador for igual a do usuário somado de 3, pois assim teremos pedra e pedra
            return 'tie'
        elif computer_input == user_input + 1 or computer_input == user_input - 2:
            # olhando em um circulo é facil de notar que essas duas condições sao equivalentes, mas como pedra pode
            # assumir valores de [0] e [3], a segunda condicional se torna necessária
            return 'lost'
        elif computer_input == user_input - 1 or computer_input == user_input + 2:
            # o mesmo do que o ultimo caso mas ao contrário
            return 'win'
        else:
            return 'somethin went wrong'
    
    def register_match_results(self, result):
        # funcao para registrar o resultados das partidas
        if result == 'win':
            self.user_wins += 1
        elif result == 'lost':
            self.computer_wins += 1
        else:
            pass
    
    def check_for_winners(self):
        #chacando para ver se alguém ganhou a melhor de 5
        if self.user_wins == 3 or self.computer_wins == 3:
            self.continue_game = not self.continue_game
        else:
            self.round += 1
        
    def game_result(self, computer_wins, user_wins):
        print('----------------')
        print('User wins: %s' % user_wins)
        print('Computer wins: %s' % computer_wins)
        
        if computer_wins > user_wins:
            print('----------------')
            print('YOU LOST!')
            print('----------------')
        elif user_wins > computer_wins:
            print('----------------')
            print('YOU WON!')
            print('----------------')
        else:
            print('----------------')
            print('You tied, try again')
    
    def reset_game(self):
        self.round = 0
        self.computer_wins = 0
        self.user_wins = 0
        self.continue_game = True
        
    
    def fair_game(self):
        print('START FAIR GAME')
        while self.continue_game:
            # pegando a jogada do usuário
            self.getUserInput()
            # print("User: ", self.user_input)
            
            # vamos colocar essa condicional para acabar o jogo com qualquer input que seja diferente dos que nós já
            # definimos anteriormente (rock, paper, scissors)
            if self.user_input not in range(0,3):
                self.reset_game()
                return 0
            
            # pegando uma jogada JUSTA do computador
            self.fair_computer()
            # print("Computer: ", self.computer)
            
            #calculando o vencedor
            win = self.calculate_winner(self.user_input, self.computer)
            
            self.register_match_results(win)
            self.check_for_winners()
            
            # printando o resultado
            print('----------------')
            print(win)
            print('----------------')
            print('User wins: %s' % self.user_wins)
            print('Computer wins: %s' % self.computer_wins)
            print('----------------')
            
        self.game_result(self.computer_wins, self.user_wins)
        self.reset_game()
            
    def unfair_game(self):
        print('START UNFAIR GAME')
        print('----------------')
        
        while self.continue_game:
            # pegando a jogada do usuário
            self.getUserInput()
            
            if self.user_input not in range(0,3):
                self.reset_game()
                return 0
            
            #pegando uma jogada INJUSTA do computador
            self.unfair_computer()
            
            #calculando o vencedor
            win = self.calculate_winner(self.user_input, self.computer)
            
            self.register_match_results(win)
            self.check_for_winners()
            
            print('----------------')
            print(win)
            print('----------------')
            print('User wins: %s' % self.user_wins)
            print('Computer wins: %s' % self.computer_wins)
            print('----------------')
            
        self.game_result(self.computer_wins, self.user_wins)
        self.reset_game()
            
game = Game()

#vamos jogar primeiro o jogo justo
game.fair_game()
#vamos jogar depois o jogo injusto
game.unfair_game()
        