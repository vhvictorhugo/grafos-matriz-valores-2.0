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
                vizinhos.append(i+1)
        return vizinhos

    def retornaVizinhos2(self, vertice): # percorre a coluna correspondente ao vértice e verifica os vizinhos
        vizinhos = []
        for i in range(len(self.matriz)):
            if (self.matriz[vertice][i][1] == 1):
                vizinhos.append(i)
        return vizinhos

    def listarVertices(self):
        vertices = []
        for i in range(len(self.matriz)):
            vertices.append(i+1)
        return vertices

    #FONTE: https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/busca-profundidade/#:~:text=O%20algoritmo%20de%20busca%20em,j%C3%A1%20visitado%2C%20retornamos%20da%20busca.
    """ Como aprendido em aula:
        Um grafo orientado é acíclico se, e somente se, não são encontrados 
        arcos de retorno durante uma busca em profundidade
    """
    def dfs_recursiva(self, vertice, visitados, flag):
        visitados.add(vertice)
        falta_visitar = [vertice]
        for vizinho in self.retornaVizinhos2(vertice):
            if vizinho not in visitados:
                visitados.add(vizinho)
                falta_visitar.append(vizinho)
                self.dfs_recursiva(vizinho, visitados,flag)
            else:
                pais = self.retornaPais(vertice)
                for pai in pais:
                    paisDosPais = self.retornaPais(pai)
                    for paiDosPais in paisDosPais:
                        if(paiDosPais not in pais):
                            pais.append(paiDosPais)
                for pai in pais:
                    if(pai == vizinho):
                        flag[0] = 1
        return flag            

    def retornaPais(self, v):   # retorna todos os pais de um vertice
        pais = []
        for i in range(len(self.matriz)):
                vizinhos = self.retornaVizinhos2(i)
                for vizinho in vizinhos:
                    if(vizinho == v):
                        pais.append(i)
        return pais

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

visited = set() # Set to keep track of visited nodes of graph.

"""
aqui iremos explorar o conceito de referencia na linguagem Python:
    quando criamos uma lista, como no caso de 'vetorSolucao', e a atribuimos a outra variavel,
    como em parâmetros de funções ou até mesmo uma simples atribuição, se não criarmos uma cópia
    é passada sua referência e portanto, você estará utilizando aquela mesma lista
"""
vetorSolucao = [False]  # indica que não há ciclos no
"""
passamos esta lista por referência em 'def_recursiva', pois é esta lista que queremos alterar ao longo das
chamadas recursivas
caso seja encontrado um arco de retorno na busca em profundidade esta lista de 1 posição é alterada de '[0]'
para '[1]'
"""
# 

# Driver Code
print("Following is the Depth-First Search")
visitados = set()
print(grafo.dfs_recursiva(0,visitados,vetorSolucao))