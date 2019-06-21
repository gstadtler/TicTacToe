'''
#-------------------------------------------------------------------------------------------------#
# Universidade Federal de Pernambuco - (UFPE)                                                     #
# Centro de Informática - (CIn)                                                                   #
# Sistemas de Informação - (SI)                                                                   #
# Algoritmos e Estruturas de Dados - (AED)                                                        #
# Projeto Final - Tic Tac Toe                                                                     #
# Alunos: Gabriel Hans Stadtler, Giovanni Evaristo Correa Junior                                  #
# Descrição: Desenvolvimento de um objeto(classe) Tabela, para auxiliar no uso dos dados do jogo, #
#            e para poder gerar um iteravel compativel para o objeto(classe) Grafo.               #
#-------------------------------------------------------------------------------------------------#
'''

class Tabuleiro:
    def __init__(self):
        # Tabuleiro do jogo
        self.__tabuleiro = ['0','1','2','3','4','5','6','7','8']
        self.__tabuleiro2 = ['9','10','11','12','13','14','15','16','17']
        self.__tabuleiro3 = ['18','19','20','21','22','23','24','25','26']
        
        # Dicionario para acessar diretamente cada posição nas linhas da tabela
        self.__row = {}
        self.__row2 = {}
        self.__row3 = {}
        
        # Dicionario para acessar diretamente cada posição nas colunas da tabela
        self.__col = {}
        self.__col2 = {}
        self.__col3 = {}
        
        # Dicionario para acessar diretamente cada posição nas diagonais da tabela
        self.__diag = {}
        self.__diag2 = {}
        self.__diag3 = {}
        
        # Lista iteravel que servirá como parâmetro para classe Grafo onde se tornará um objeto do tipo Grafo Direcionado e Ponderado
        self.__iterable = []
        self.__iterable2 = []
        self.__iterable3 = []

    @property
    def tabuleiro(self):
        return self.__tabuleiro
    @property
    def tabuleiro2(self):
        return self.__tabuleiro2
    @property
    def tabuleiro3(self):
        return self.__tabuleiro3
    @property
    def row(self):
        return self.__row
    @property
    def row2(self):
        return self.__row2
    @property
    def row3(self):
        return self.__row3
    @property
    def col(self):
        return self.__col
    @property
    def col2(self):
        return self.__col2
    @property
    def col3(self):
        return self.__col3
    @property
    def diag(self):
        return self.__diag
    @property
    def diag2(self):
        return self.__diag2
    @property
    def diag3(self):
        return self.__diag3
    @property
    def iterable(self):
        return self.__iterable
    @property
    def iterable2(self):
        return self.__iterable2
    @property
    def iterable3(self):
        return self.__iterable3

    def gerar_linhas(self,iteravel,iteravel2,iteravel3):
        # Definindo as linhas num dicionario para linhas do tabuleiro
        self.row["L1"]= [iteravel[0],iteravel[1],iteravel[2]]
        self.row["L2"]= [iteravel[3],iteravel[4],iteravel[5]]
        self.row["L3"]= [iteravel[6],iteravel[7],iteravel[8]]
        # tabuleiro 2
        self.row2["L1"]= [iteravel2[0],iteravel2[1],iteravel2[2]]
        self.row2["L2"]= [iteravel2[3],iteravel2[4],iteravel2[5]]
        self.row2["L3"]= [iteravel2[6],iteravel2[7],iteravel2[8]]
        # tabuleiro 3
        self.row3["L1"]= [iteravel3[0],iteravel3[1],iteravel3[2]]
        self.row3["L2"]= [iteravel3[3],iteravel3[4],iteravel3[5]]
        self.row3["L3"]= [iteravel3[6],iteravel3[7],iteravel3[8]]

    def gerar_colunas(self,iteravel,iteravel2,iteravel3):
        # Definindo as colunas num dicionario para colunas do tabuleiro
        self.col["C1"]= [iteravel[0],iteravel[3],iteravel[6]]
        self.col["C2"]= [iteravel[1],iteravel[4],iteravel[7]]
        self.col["C3"]= [iteravel[2],iteravel[5],iteravel[8]]
        # tabuleiro 2
        self.col2["C1"]= [iteravel2[0],iteravel2[3],iteravel2[6]]
        self.col2["C2"]= [iteravel2[1],iteravel2[4],iteravel2[7]]
        self.col2["C3"]= [iteravel2[2],iteravel2[5],iteravel2[8]]
        # tabuleiro 3
        self.col3["C1"]= [iteravel3[0],iteravel3[3],iteravel3[6]]
        self.col3["C2"]= [iteravel3[1],iteravel3[4],iteravel3[7]]
        self.col3["C3"]= [iteravel3[2],iteravel3[5],iteravel3[8]]
            
    def gerar_diagonais(self,iteravel,iteravel2,iteravel3):
        # Definindo as diagonais num dicionario para diagonais do tabuleiro
        self.diag["D1"]= [iteravel[0],iteravel[4],iteravel[8]]
        self.diag["D2"]= [iteravel[2],iteravel[4],iteravel[6]]
        # tabuleiro 2
        self.diag2["D1"]= [iteravel2[0],iteravel2[4],iteravel2[8]]
        self.diag2["D2"]= [iteravel2[2],iteravel2[4],iteravel2[6]]
        # tabuleiro 3
        self.diag3["D1"]= [iteravel3[0],iteravel3[4],iteravel3[8]]
        self.diag3["D2"]= [iteravel3[2],iteravel3[4],iteravel3[6]]

    def gerar_iterable4graph(self):
        # Definindo um iteravel que quando passada como parâmetro para a classe Grafo, se torna um Grafo Direcionado e Ponderado
        col = self.col
        row = self.row
        col2 = self.col2
        row2 = self.row2
        col3 = self.col3
        row3 = self.row3
                    
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

        # tabuleiro 2
        self.__iterable2 = [
        ((col2['C1'][0],row2['L1'][1]),1), ((col2['C1'][0],row2['L2'][0]),1), ((col2['C1'][0],row2['L2'][1]),1),
        ((col2['C2'][0],row2['L1'][0]),1), ((col2['C2'][0],row2['L1'][2]),1), ((col2['C2'][0],row2['L2'][0]),1), ((col2['C2'][0],row2['L2'][1]),1), ((col2['C2'][0],row2['L2'][2]),1),
        ((col2['C3'][0],row2['L1'][1]),1), ((col2['C3'][0],row2['L2'][1]),1), ((col2['C3'][0],row2['L2'][2]),1), 
        ((col2['C1'][1],row2['L1'][0]),1), ((col2['C1'][1],row2['L1'][1]),1), ((col2['C1'][1],row2['L2'][1]),1), ((col2['C1'][1],row2['L3'][0]),1), ((col2['C1'][1],row2['L3'][1]),1),
        ((col2['C2'][1],row2['L1'][0]),1), ((col2['C2'][1],row2['L1'][1]),1), ((col2['C2'][1],row2['L1'][2]),1), ((col2['C2'][1],row2['L2'][0]),1), ((col2['C2'][1],row2['L2'][2]),1), ((col['C2'][1],row['L3'][0]),1), ((col['C2'][1],row['L3'][1]),1), ((col['C2'][1],row['L3'][2]),1),
        ((col2['C3'][1],row2['L1'][1]),1), ((col2['C3'][1],row2['L1'][2]),1), ((col2['C3'][1],row2['L2'][1]),1), ((col2['C3'][1],row2['L3'][1]),1), ((col2['C3'][1],row2['L3'][2]),1),
        ((col2['C1'][2],row2['L2'][0]),1), ((col2['C1'][2],row2['L2'][1]),1), ((col2['C1'][2],row2['L3'][1]),1),
        ((col2['C2'][2],row2['L2'][0]),1), ((col2['C2'][2],row2['L2'][1]),1), ((col2['C2'][2],row2['L2'][2]),1), ((col2['C2'][2],row2['L3'][0]),1), ((col2['C2'][2],row2['L3'][2]),1),
        ((col2['C3'][2],row2['L2'][1]),1), ((col2['C3'][2],row2['L2'][2]),1), ((col2['C3'][2],row2['L3'][1]),1)
        ]

        # tabuleiro 3
        self.__iterable3 = [
        ((col3['C1'][0],row3['L1'][1]),1), ((col3['C1'][0],row3['L2'][0]),1), ((col3['C1'][0],row3['L2'][1]),1),
        ((col3['C2'][0],row3['L1'][0]),1), ((col3['C2'][0],row3['L1'][2]),1), ((col3['C2'][0],row3['L2'][0]),1), ((col3['C2'][0],row3['L2'][1]),1), ((col3['C2'][0],row3['L2'][2]),1),
        ((col3['C3'][0],row3['L1'][1]),1), ((col3['C3'][0],row3['L2'][1]),1), ((col3['C3'][0],row3['L2'][2]),1), 
        ((col3['C1'][1],row3['L1'][0]),1), ((col3['C1'][1],row3['L1'][1]),1), ((col3['C1'][1],row3['L2'][1]),1), ((col3['C1'][1],row3['L3'][0]),1), ((col3['C1'][1],row3['L3'][1]),1),
        ((col3['C2'][1],row3['L1'][0]),1), ((col3['C2'][1],row3['L1'][1]),1), ((col3['C2'][1],row3['L1'][2]),1), ((col3['C2'][1],row3['L2'][0]),1), ((col3['C2'][1],row3['L2'][2]),1), ((col['C2'][1],row['L3'][0]),1), ((col['C2'][1],row['L3'][1]),1), ((col['C2'][1],row['L3'][2]),1),
        ((col3['C3'][1],row3['L1'][1]),1), ((col3['C3'][1],row3['L1'][2]),1), ((col3['C3'][1],row3['L2'][1]),1), ((col3['C3'][1],row3['L3'][1]),1), ((col3['C3'][1],row3['L3'][2]),1),
        ((col3['C1'][2],row3['L2'][0]),1), ((col3['C1'][2],row3['L2'][1]),1), ((col3['C1'][2],row3['L3'][1]),1),
        ((col3['C2'][2],row3['L2'][0]),1), ((col3['C2'][2],row3['L2'][1]),1), ((col3['C2'][2],row3['L2'][2]),1), ((col3['C2'][2],row3['L3'][0]),1), ((col3['C2'][2],row3['L3'][2]),1),
        ((col3['C3'][2],row3['L2'][1]),1), ((col3['C3'][2],row3['L2'][2]),1), ((col3['C3'][2],row3['L3'][1]),1)
        ]

    def atualizar_tabuleiro(self):
        # Método que atualiza o tabuleiro a cada jogada
        self.gerar_linhas(self.tabuleiro,self.tabuleiro2,self.tabuleiro3)
        self.gerar_colunas(self.tabuleiro,self.tabuleiro2,self.tabuleiro3)
        self.gerar_diagonais(self.tabuleiro,self.tabuleiro2,self.tabuleiro3)
        self.gerar_iterable4graph()

    def limpar_tabuleiro(self):
        self.__tabuleiro = ['0','1','2','3','4','5','6','7','8']
        self.__tabuleiro2 = ['9','10','11','12','13','14','15','16','17']
        self.__tabuleiro3 = ['18','19','20','21','22','23','24','25','26']
        
    def __repr__(self):
        rep = '''
        0 | 1 | 2    9 | 10 | 11   18 | 19 | 20  
        ---------   ------------   ------------
        3 | 4 | 5   12 | 13 | 14   21 | 22 | 23
        ---------   ------------   ------------
        6 | 7 | 8   15 | 16 | 17   24 | 25 | 26
              '''
        return rep
        
    def __str__(self):
        tabuleiro_jogo = '{} | {} | {}    {} | {} | {}   {} | {} | {}\n---------   ------------   ------------\n{} | {} | {}   {} | {} | {}   {} | {} | {}\n---------   ------------   ------------\n{} | {} | {}   {} | {} | {}   {} | {} | {}'.format(self.row['L1'][0],self.row['L1'][1],self.row['L1'][2],
                                                                                                                                                                                                                                                       self.row2['L1'][0],self.row2['L1'][1],self.row2['L1'][2],
                                                                                                                                                                                                                                                       self.row3['L1'][0],self.row3['L1'][1],self.row3['L1'][2],
                                                                                                                                                                                                                                                       self.row['L2'][0],self.row['L2'][1],self.row['L2'][2],
                                                                                                                                                                                                                                                       self.row2['L2'][0],self.row2['L2'][1],self.row2['L2'][2],
                                                                                                                                                                                                                                                       self.row3['L2'][0],self.row3['L2'][1],self.row3['L2'][2],
                                                                                                                                                                                                                                                       self.row['L3'][0],self.row['L3'][1],self.row['L3'][2],
                                                                                                                                                                                                                                                       self.row2['L3'][0],self.row2['L3'][1],self.row2['L3'][2],
                                                                                                                                                                                                                                                       self.row3['L3'][0],self.row3['L3'][1],self.row3['L3'][2])
        return tabuleiro_jogo


t = Tabuleiro()
t.atualizar_tabuleiro()
