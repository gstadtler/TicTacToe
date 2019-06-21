'''
#-------------------------------------------------------------------------------------------------#
# Universidade Federal de Pernambuco - (UFPE)                                                     #
# Centro de Informática - (CIn)                                                                   #
# Sistemas de Informação - (SI)                                                                   #
# Algoritmos e Estruturas de Dados - (AED)                                                        #
# Projeto Final - Tic Tac Toe                                                                     #
# Alunos: Gabriel Hans Stadtler, Giovanni Evaristo Correa Junior                                  #
# Descrição: Desenvolvimento de um objeto(classe) do tipo Jogo, onde estão as funcionalidades do  #
#            jogo Tic Tac Toe - Notakto.                                                          #
#-------------------------------------------------------------------------------------------------#
'''

from tabuleiro_notakto import Tabuleiro
from digrafoPonderado import DigrafoPonderado
import time

class Jogo:
    def __init__(self):
        # Inicia as outras classes que provem os dados para o jogo
        self.tab = Tabuleiro()
        
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
                            
    def derrota(self,pos):
        if self.tab.pos['L1'] == ['x','x','x']:
            return True
        elif self.tab.pos['L2'] == ['x','x','x']:
            return True
        elif self.tab.pos['L3'] == ['x','x','x']:
            return True
        elif self.tab.pos['C1'] == ['x','x','x']:
            return True
        elif self.tab.pos['C2'] == ['x','x','x']:
            return True
        elif self.tab.pos['C3'] == ['x','x','x']:
            return True
        elif self.tab.pos['D1'] == ['x','x','x']:
            return True
        elif self.tab.pos['D2'] == ['x','x','x']:
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

    def jogada_player1(self,tabul,jogada):
        # Analisa se o movimento e valido e seta tal movimento no tabuleiro
        
        if self.movimento_valido(jogada):
            self.tab.tabul[jogada] = 'x'
            self.tab.atualizar_tabul()
            return self.tab.tabul[jogada]

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
                        return False

            else:
                pass

    def main(self):
        # Metodo que inicia o jogo, chamando os demais metodos da classe que
        # fomentam o jogo e finalmente faz o jogo rodar ate que um dos players percam
        #
        
        game_over = False
        print('BEM-VINDO AO NOTAKTO')
        while game_over != True:
            self.tab1.atualizar_tabuleiro()
            self.tab2.atualizar_tabuleiro()
            self.tab3.atualizar_tabuleiro()
            print('{}  {}  {}'.format(self.tab1,self.tab2,self.tab3))
            jogador1 = int(input('Esolha uma posição: '))
            human_turn = self.jogadas.append((self.jogada_player1(jogador1),self.player1))
            self.tab1.atualizar_tabuleiro()
            time.sleep(0.3)
            print(self.tab1,self.tab2,self.tab3)
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

        print(self.tab1,self.tab2l,self.tab3)
        print('FIM DE JOGO')
        print('JOGADOR: {} PERDEU!'.format(perdedor))
        play_again = input('Jogar novamente?\n(s/n): ')
        if play_again == 's':
            self.tab1.limpar_tabuleiro()
            self.main()

notakto = Jogo()
notakto.main()

            
                
