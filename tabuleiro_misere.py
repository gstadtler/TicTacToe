'''
#-------------------------------------------------------------------------------------------------#
# Universidade Federal de Pernambuco - (UFPE)                                                     #
# Centro de Informática - (CIn)                                                                   #
# Sistemas de Informação - (SI)                                                                   #
# Algoritmos e Estruturas de Dados - (AED)                                                        #
# Projeto Final - Tic Tac Toe                                                                     #
# Alunos: Gabriel Hans Stadtler (ghs2), Giovanni Evaristo Correa Junior (gecj)                                  #
# Descrição: Desenvolvimento de um objeto(classe) Tabela, para auxiliar no uso dos dados do jogo, #
#            e para poder gerar um iteravel compativel para o objeto(classe) Grafo.               #
#-------------------------------------------------------------------------------------------------#
'''

class Tabuleiro:
    def __init__(self):
        # Tabuleiro do jogo
        self.__tabuleiro = ['0','1','2','3','4','5','6','7','8']
        
        # Dicionario para acessar diretamente cada posição nas linhas da tabela
        self.__row = {}
        
        # Dicionario para acessar diretamente cada posição nas colunas da tabela
        self.__col = {}
        
        # Dicionario para acessar diretamente cada posição nas diagonais da tabela
        self.__diag = {}
        
        # Lista iteravel que servirá como parâmetro para classe Grafo onde se tornará um objeto do tipo Grafo Direcionado e Ponderado
        self.__iterable = []

    @property
    def tabuleiro(self):
        return self.__tabuleiro
    @property
    def row(self):
        return self.__row
    @property
    def col(self):
        return self.__col
    @property
    def diag(self):
        return self.__diag
    @property
    def iterable(self):
        return self.__iterable

    def gerar_linhas(self,iteravel):
        # Definindo as linhas num dicionario para linhas do tabuleiro
        self.row["L1"]= [iteravel[0],iteravel[1],iteravel[2]]
        self.row["L2"]= [iteravel[3],iteravel[4],iteravel[5]]
        self.row["L3"]= [iteravel[6],iteravel[7],iteravel[8]]

    def gerar_colunas(self,iteravel):
        # Definindo as colunas num dicionario para colunas do tabuleiro
        self.col["C1"]= [iteravel[0],iteravel[3],iteravel[6]]
        self.col["C2"]= [iteravel[1],iteravel[4],iteravel[7]]
        self.col["C3"]= [iteravel[2],iteravel[5],iteravel[8]]    
            
    def gerar_diagonais(self,iteravel):
        # Definindo as diagonais num dicionario para diagonais do tabuleiro
        self.diag["D1"]= [iteravel[0],iteravel[4],iteravel[8]]
        self.diag["D2"]= [iteravel[2],iteravel[4],iteravel[6]]

    def gerar_iterable4graph(self):
        # Definindo um iteravel que quando passada como parâmetro para a classe Grafo, se torna um Grafo Direcionado e Ponderado
        col = self.col
        row = self.row
                    
        self.__iterable = [
        ((col['C1'][0],row['L1'][1]),1), ((col['C1'][0],row['L2'][0]),1), ((col['C1'][0],row['L2'][1]),1),
        ((col['C2'][0],row['L1'][0]),1), ((col['C2'][0],row['L1'][2]),1), ((col['C2'][0],row['L2'][0]),1), ((col['C2'][0],row['L2'][1]),1), ((col['C2'][0],row['L2'][2]),1),
        ((col['C3'][0],row['L1'][1]),1), ((col['C3'][0],row['L2'][1]),1), ((col['C3'][0],row['L2'][2]),1), 
        ((col['C1'][1],row['L1'][0]),1), ((col['C1'][1],row['L1'][1]),1), ((col['C1'][1],row['L2'][1]),1), ((col['C1'][1],row['L3'][0]),1), ((col['C1'][1],row['L3'][1]),1),
        ((col['C2'][1],row['L1'][0]),1), ((col['C2'][1],row['L1'][1]),1), ((col['C2'][1],row['L1'][2]),1), ((col['C2'][1],row['L2'][0]),1), ((col['C2'][1],row['L2'][2]),1), ((col['C2'][1],row['L3'][0]),1), ((col['C2'][1],row['L3'][1]),1), ((col['C2'][1],row['L3'][2]),1),
        ((col['C3'][1],row['L1'][1]),1), ((col['C3'][1],row['L1'][2]),1), ((col['C3'][1],row['L2'][1]),1), ((col['C3'][1],row['L3'][1]),1), ((col['C3'][1],row['L3'][2]),1),
        ((col['C1'][2],row['L2'][0]),1), ((col['C1'][2],row['L2'][1]),1), ((col['C1'][2],row['L3'][1]),1),
        ((col['C2'][2],row['L2'][0]),1), ((col['C2'][2],row['L2'][1]),1), ((col['C2'][2],row['L2'][2]),1), ((col['C2'][2],row['L3'][0]),1), ((col['C2'][2],row['L3'][2]),1),
        ((col['C3'][2],row['L2'][1]),1), ((col['C3'][2],row['L2'][2]),1), ((col['C3'][2],row['L3'][1]),1)
        ]

    def atualizar_tabuleiro(self):
        # Método que atualiza o tabuleiro a cada jogada
        self.gerar_linhas(self.tabuleiro)
        self.gerar_colunas(self.tabuleiro)
        self.gerar_diagonais(self.tabuleiro)
        self.gerar_iterable4graph()

    def limpar_tabuleiro(self):
        self.__tabuleiro = ['0','1','2','3','4','5','6','7','8']
        
    def __repr__(self):
        rep = '''
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
              '''
        return rep
        
    def __str__(self):
        tabuleiro_jogo = '{} | {} | {}\n---------\n{} | {} | {}\n---------\n{} | {} | {}'.format(self.row['L1'][0],self.row['L1'][1],self.row['L1'][2],
                                                                                                 self.row['L2'][0],self.row['L2'][1],self.row['L2'][2],
                                                                                                 self.row['L3'][0],self.row['L3'][1],self.row['L3'][2])        
        return tabuleiro_jogo
