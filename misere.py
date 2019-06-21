'''
#-------------------------------------------------------------------------------------------------#
# Universidade Federal de Pernambuco - (UFPE)                                                     #
# Centro de Informática - (CIn)                                                                   #
# Sistemas de Informação - (SI)                                                                   #
# Algoritmos e Estruturas de Dados - (AED)                                                        #
# Projeto Final - Tic Tac Toe                                                                     #
# Alunos: Gabriel Hans Stadtler (ghs2), Giovanni Evaristo Correa Junior (gecj)                                 #
# Descrição: Desenvolvimento de um objeto(classe) do tipo Jogo, onde estão as funcionalidades do  #
#            jogo Tic Tac Toe - Misere.                                                           #
#-------------------------------------------------------------------------------------------------#
'''

from tabuleiro_misere import Tabuleiro
from digrafoPonderado import DigrafoPonderado
import time

class Jogo:
    def __init__(self):
        # Inicia as outras classes que provem os dados para o jogo
        self.tab = Tabuleiro()
        self.grafo = DigrafoPonderado(self.tab.iterable)
        
        # Atributos que definem o Jogador 1 e suas pontuacoes
        self.player1 = 'HUMANO'
        self.pontos_humano = 0
        
        # Atributos que definem o Jogador 2 e suas pontuacoes
        self.player2 = 'MAQUINA'
        self.pontos_maquina = 0
        
        # Lista de jogadas
        self.jogadas = []
        
    def pontuacao(self):
        if self.loser == 'MAQUINA':
            self.pontos_humano += 1
        else:
            self.pontos_maquina += 1
                            
    def derrota(self):
        if self.tab.row['L1'] == ['x','x','x']:
            return True
        elif self.tab.row['L2'] == ['x','x','x']:
            return True
        elif self.tab.row['L3'] == ['x','x','x']:
            return True
        elif self.tab.col['C1'] == ['x','x','x']:
            return True
        elif self.tab.col['C2'] == ['x','x','x']:
            return True
        elif self.tab.col['C3'] == ['x','x','x']:
            return True
        elif self.tab.diag['D1'] == ['x','x','x']:
            return True
        elif self.tab.diag['D2'] == ['x','x','x']:
            return True
        else:
            return False

    def loser(self):
        # Metodo que define o jogador perdedor atraves da lista de jogadas
        return self.jogadas[len(self.jogadas)-1][1]

    def movimento_valido(self,jogada):
        # Metodo que retornar se a jogada e valida, analisando se
        # tal posição ja foi marcada no tabuleiro
        
        if jogada == 'x':
            return False
        elif self.tab.tabuleiro[jogada] != 'x':
            return True
        else:
            return False

    def game_over(self):
        # Metodo que analisa se o jogo acabou e retorna quem perdeu o jogo
        
        losP1 = self.derrota()
        losP2 = self.derrota()
        return losP1 or losP2

    ### JOGADORES ###

    def jogada_player1(self,jogada):
        # Analisa se o movimento e valido e seta tal movimento no tabuleiro
        
        if self.movimento_valido(jogada):
            self.tab.tabuleiro[jogada] = 'x'
            self.tab.atualizar_tabuleiro()
            return self.tab.tabuleiro[jogada]
        else:
            return False

    def jogada_player2(self):
        # Ao analisar se as possiveis jogadas levam a uma condicao de vitoria
        # atraves do metodo de busca da classe grafo
        # seta no tabuleiro o movimento da maquina
        
        # Atualiza o tabuleiro e o grafo
        self.tab.atualizar_tabuleiro()
        self.grafo = DigrafoPonderado(self.tab.iterable)
        
        # Para todo vertice pertencente ao grafo
        # analisa se o mesmo leva para uma condicao de vitoria
        for v in self.grafo.vertex:
            if v != 'x':
                if self.movimento_valido(int(v)):
                    self.grafo.bfs(v)
                    if v in self.grafo.antecessores['x']:
                        self.tab.tabuleiro[int(v)] = 'x'
                        self.tab.atualizar_tabuleiro()
                        return self.tab.tabuleiro[int(v)]
                    else:
                        pass
                        
            else:
                pass

    def main(self):
        # Metodo que inicia o jogo, chamando os demais metodos da classe que
        # fomentam o jogo e finalmente faz o jogo rodar ate que um dos players percam
        #
        
        game_over = False
        print('BEM-VINDO AO MISERE')
        while game_over != True:
            self.tab.atualizar_tabuleiro()
            print(self.tab)
            jogador1 = int(input('Esolha uma posição: '))
            human_turn = self.jogada_player1(jogador1)
            while human_turn == False:
                new_try = int(input('JOGADA INVÁLIDA - Escolha outra posição: '))
                human_turn = self.jogada_player1(new_try)
            self.jogadas.append((human_turn,self.player1))
            self.tab.atualizar_tabuleiro()
            time.sleep(0.3)
            print(self.tab)
            game_over = self.game_over()
            perdedor = self.loser()
            if game_over:
                break
            else:
                print('Turno da máquina. . .')
                time.sleep(1.5)
                machine_turn = self.jogadas.append((self.jogada_player2(),self.player2))
                game_over = self.game_over()
                perdedor = self.loser()

        print(self.tab)
        print('FIM DE JOGO')
        print('JOGADOR: {} PERDEU!'.format(perdedor))
        play_again = input('Jogar novamente?\n(s/n): ')
        if play_again == 's':
            self.tab.limpar_tabuleiro()
            self.main()

misere = Jogo()
misere.main()
