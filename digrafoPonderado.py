'''
#-------------------------------------------------------------------------------------------------#
# Universidade Federal de Pernambuco - (UFPE)                                                     #
# Centro de Informática - (CIn)                                                                   #
# Sistemas de Informação - (SI)                                                                   #
# Algoritmos e Estruturas de Dados - (AED)                                                        #
# Projeto Final - Tic Tac Toe                                                                     #
# Alunos: Gabriel Hans Stadtler (ghs2), Giovanni Evaristo Correa Junior (gecj)                                  #
# Descrição: Desenvolvimento de um objeto(classe) TAD Grafo Direcionado e Ponderado para o        #
#            tratamento de dados do Jogo Tic Tac Toe.                                             #
#-------------------------------------------------------------------------------------------------#
'''

class DigrafoPonderado:
    def __init__(self,iterable):
        self.vertex = {}
        self.nEdges = 0
        for i in iterable:
            j = i[0][0]
            u = i[0][1]
            value = i[1]
            if j not in self.vertex:
                self.vertex[j]= []
            if u not in self.vertex:
                self.vertex[u]= []
            self.insertEdge(j,u,value)     

    def vertexInGraph(self,v):
        return v in self.vertex

    def getVertices(self):
       return [v for v in self.vertex]

    def insertVertex(self,v):
        if self.vertexInGraph(v) == False:
            self.vertex[v]= []
        else:
            return False

    def edgeInGraph(self,v,u):
        if self.vertexInGraph(v) == True:
            return u in self.vertex[v]
        else:
            return False

    def insertEdge(self,v,u,value):
        if self.edgeInGraph(v,u) == False:
            self.vertex[v].append((u,value))
            self.nEdges += 1
            return True
        else:
            return False

    def getAdjacent(self,v):
        adjacent = []
        if self.vertexInGraph(v):
            for i in self.vertex[v]:
                adjacent.append(i[0])
            return adjacent
        else:
            return False

    def getEdges(self):
        vertices = [x for x in self.vertex.keys()]
        edges = []
        for v in vertices:
            adj = self.getAdjacent(v)
            for u in adj:
                edges.append((v,u))
        return edges

    def getEdgeWeight(self,v,u):
        weight = 0
        if v not in self.vertex:
            return False
        else:
            for x in self.vertex[v]:
                if u == x[0]:
                    weight = x[1]
            return weight
            
            
    def degree(self,v):
        if self.vertexInGraph(v):
            if self.vertex[v] == []:
                return 0
            return len(self.vertex[v])
        else:
            return False

    # METODOS ESPECIAIS
    
    def __repr__(self):
        return "A {} vertices and {} edges Graph".format(len(self.vertex),self.nEdges)
            
    # METODOS DE BUSCA
    
    def bfs(self,raiz):
        inf = 999999
        self.cor = {}
        self.antecessores = {}
        self.distancia = {}
        for v in self.getVertices():
            self.cor[v] = 'branco'
            self.antecessores[v] = None
            self.distancia[v] = inf

        self.cor[raiz] = 'cinza'
        self.distancia[raiz] = 0
        fila = [raiz]

        while fila != []:
            u = fila.pop(0)
            for v in self.getAdjacent(u):
                if self.cor[v] == 'branco':
                    fila.append(v)
                    self.cor[v] = 'cinza'
                    self.antecessores[v] = u
                    self.distancia[v] = self.distancia[u]+1
                    self.cor[u] = 'preto'

        return self.antecessores,self.distancia

    def dfs(self):
        self.color = {}
        self.prev = {}
        self.distance = {}
        for v in self.getVertices():
            self.color[v] = 'branco'
            self.prev[v] = None
            self.distance[v] = 0

        for v in self.getVertices():
            if self.color[v] == 'branco':
                self.dfs_visiting(v)

    def dfs_visiting(self,v):
        self.distance[v] += 1
        self.color[v] = 'cinza'
        for u in self.getAdjacent(v):
            if self.color[u] == 'branco':
                self.prev[u] = v
                self.dfs_visiting(v)
        self.color[v] = 'preto'
        self.distance[v] += 1

    # METODO DE MENOR CAMINHO
        
    def dijkstra(self,source):
        src = source
        visitedV = {}
        unvisitedV = [v for v in graph.vertex.keys()]
        inf = 9999999
        costs = {}
        prev = {}
        for v in unvisitedV:
            prev[v]= None
            if v != src:
                costs[v]= inf
            else:
                costs[v]= 0

        while len(visitedV) != len(unvisitedV):
            for v in unvisitedV:
                if v == src:
                    minimum = []
                    for u in graph.getAdjacent(v):
                        if u not in visitedV:
                            peso = graph.getEdgeWeight(v,u)
                            if costs[u] > costs[v] + peso:
                                costs[u]= costs[v] + peso
                                prev[u]= v
                                minimum.append(costs[u])
                            else:
                                nextSrc = u
                        else:
                            minimum.append(costs[u])
                            nextSrc = prev[v]

                    for i in costs:
                        if costs[i] == min(minimum):
                            visitedV[src]= i
                            if i not in visitedV:
                                src = i
                            else:
                                src = nextSrc
                
        return costs,prev
