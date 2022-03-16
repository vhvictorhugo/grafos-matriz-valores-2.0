class Grafo(object):
    def __init__(self):  # inicializa as estruturas base do grafo
        self.matriz = []

    def inicializaMatriz(self, n):  # inicializa a matriz de valores com 0
        posicao = [0, 0]    # por default, uma posicao recebe peso (p) 0 e valor 0 para orientacao (o) de arco, sendo:
        for i in range(n):          # 1: se o arco tem origem no vértice i, -1: se i é o vértice destino do arco e 0: se nao há arco para o vértice i
            self.matriz.append([posicao].copy() * n)

    def mostraMatriz(self):
        for linha in self.matriz:
            print(linha,"\n")

    def atribuiPosicao(self, linha, coluna, peso):  # atribui os pesos e direções dos arcos na matriz

        self.matriz[linha - 1][coluna - 1] = [peso, +1]
        self.matriz[coluna - 1][linha - 1] = [peso,-1]
        
    def retornaVizinhos(self, vertice): # percorre a coluna correspondente ao vértice e verifica os vizinhos
        vizinhos = []
        for i in range(len(self.matriz)):
            if (self.matriz[vertice][i][1] == 1):
                vizinhos.append(i + 1)
        return vizinhos

    def listarVertices(self):
        vertices = []
        for i in range(len(self.matriz)):
            vertices.append(i+1)
        return vertices
    #FONTE: https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/busca-profundidade/#:~:text=O%20algoritmo%20de%20busca%20em,j%C3%A1%20visitado%2C%20retornamos%20da%20busca.
    def dfs_recursiva(self, vertice, visitados):
        visitados.add(vertice)
        falta_visitar = [vertice]
        for vizinho in self.listarVertices():
            if vizinho not in visitados:
                visitados.add(vizinho)
                falta_visitar.append(vizinho)
                self.dfs_recursiva(vizinho, visitados)
            else:
                if(self.ehDescendente(vertice, vizinho)):
                    return False

    def ehDescendente(self, v, w):
        pais = []
        for i in range(len(self.matriz)):
            if (self.retornaVizinhos(i) == v):
                pais.append(i)
                for p in pais:
                    self.ehDescendente(pais.index(p, w))
        if(w in pais):
            return True
        
    
    # def dfs(self):
    #     visitados = set()   # vértices marcados

    #     def dfs_iterativa(vertice_fonte):
            
    #         visitados.add(vertice_fonte)
    #         vertices = self.listarVertices()                    # lista de vértices restantes
    #         falta_visitar = [vertice_fonte]                     # vértices a visitar
    #         while falta_visitar:                                # enquanto existir vertice nao visitado
    #             vertice = falta_visitar.pop()
    #             for vizinho in self.retornaVizinhos(vertice-1):   # percorre vizinhos do vértice v
    #                 if vizinho not in visitados:                # se w é não marcado
    #                     visitados.add(vizinho)
    #                     falta_visitar.append(vizinho)
    #                     vertices.remove()
    #                 else: # explora arestas que não fazem parte da árvore de profundidade
    #                     """
    #                     Sabemos que:
    #                     • Um grafo orientado é acíclico se, e somente se, não são encontrados arcos de retorno 
    #                     durante uma busca em profundidade e também sabemos que:
    #                     • Se v é descendente de w na floresta/árvore, então é um arco de retorno.
    #                     • v: vertice; w: vizinho
    #                     """
    #                     if(vertice in self.retornaVizinhos(vizinho-1)):
    # #                         return False
    #     contFalsos = 0
    #     if(grafo.dfs_recursiva(1) == False):
    #         contFalsos += 1

    #     if(contFalsos == 0):
    #         return False
    #     else:
    #         return True
        

    """
    def dfs(self, visited, node):  #function for dfs 
        if node not in visited:
            print (node)
            visited.add(node)            
            for neighbour in self.retornaVizinhos(node-1):
                self.dfs(visited, neighbour)
    """

    # FONTE: https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/ordenacao-topologica/
    def ordenacao_topologica(self):
        # citar na documentacao: numeracao de vertices deve comecar a partir de 1
        # Ordenação topológica baseada no grau de entrada dos vértices
        ordem_topologica = []
        # Calcula graus de entrada.
        graus_entrada = [0 for _ in range(len(self.matriz))]
        for i in range(len(self.matriz)):
            listaVizinhos = self.retornaVizinhos(i)
            for vizinho in listaVizinhos:
                graus_entrada[vizinho-1] += 1
        # Cria uma fila de vértices com grau de entrada zero.
        fila = [v for v in range(len(self.matriz)) if graus_entrada[v] == 0]
        while fila:
            vertice = fila.pop()
            ordem_topologica.append(vertice+1)
            # Atualiza o grau de entrada dos vizinhos.
            listaVizinhos = self.retornaVizinhos(vertice)
            for vizinho in listaVizinhos:
                graus_entrada[vizinho-1] -= 1
                # Algum dos vizinhos passou a ter grau de entrada zero.
                if graus_entrada[vizinho-1] == 0:
                    fila.append(vizinho-1)
        return ordem_topologica

grafo = Grafo()
nomeArquivo = "grafo.txt"
arquivo = open(f'.\\src\\{nomeArquivo}', 'r')
n = int(arquivo.readline())
grafo.inicializaMatriz(n)
for linha in arquivo:
    linha = linha.split(' ')
    grafo.atribuiPosicao((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))
arquivo.close()

#print("Grafo possui ciclo?", grafo.verificaCiclo())
# print("Ordenacao Topologica:", grafo.ordenacao_topologica())
# print("Busca: ", grafo.dfs(1))
visited = set() # Set to keep track of visited nodes of graph.
# Driver Code
print("Following is the Depth-First Search")
visitados = set()
print(grafo.dfs_recursiva(1,visitados))