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

    def dfs(grafo, vertice):
        visitados = set()

        def dfs_iterativa(grafo, vertice_fonte):
            visitados.add(vertice_fonte)
            falta_visitar = [vertice_fonte]
            while falta_visitar:
                vertice = falta_visitar.pop()
                for vizinho in grafo[vertice]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        falta_visitar.append(vizinho)

        dfs_iterativa(grafo, vertice)
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
nomeArquivo = "grafo_t.txt"
arquivo = open(f'.\\src\\{nomeArquivo}', 'r')
n = int(arquivo.readline())
grafo.inicializaMatriz(n)
for linha in arquivo:
    linha = linha.split(' ')
    grafo.atribuiPosicao((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))
arquivo.close()

#print("Grafo possui ciclo?", grafo.verificaCiclo())
print("Ordenacao Topologica:", grafo.ordenacao_topologica())
# print("Busca: ", grafo.dfs(1))
visited = set() # Set to keep track of visited nodes of graph.
# Driver Code
print("Following is the Depth-First Search")
grafo.dfs(visited, 1)