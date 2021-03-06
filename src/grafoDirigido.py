class GrafoDirigido(object):
    def __init__(self):  # inicializa as estruturas base do grafo
        self.matriz = []

    def inicializaMatriz(self, n):  # inicializa a matriz de valores com 0
        posicao = [0, 0]    # por default, uma posicao recebe peso (p) 0 e valor 0 para orientacao (o) de arco, sendo:
        for i in range(n):          # 1: se o arco tem origem no vértice i, -1: se i é o vértice destino do arco e 0: se nao há arco para o vértice i
            self.matriz.append([posicao].copy() * n)    

    def atribuiPosicao(self, linha, coluna, peso):  # atribui os pesos e direções dos arcos na matriz

        self.matriz[linha - 1][coluna - 1] = [peso, +1]
        self.matriz[coluna - 1][linha - 1] = [peso,-1]

    def mostraMatriz(self):
        for linha in self.matriz:
            print(linha,"\n")
        
    def retornaVizinhos(self, vertice): # percorre a coluna correspondente ao vértice e verifica os vizinhos
        vizinhos = []
        for i in range(len(self.matriz)):
            if (self.matriz[vertice][i][1] == 1):
                vizinhos.append(i+1)
        return vizinhos

    def listarVertices(self):
        vertices = []
        for i in range(len(self.matriz)):
            vertices.append(i+1)
        return vertices

    """ Como aprendido em aula:
        Um grafo orientado é acíclico se, e somente se, não são encontrados 
        arcos de retorno durante uma busca em profundidade
    """
    #FONTE: https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/busca-profundidade/#:~:text=O%20algoritmo%20de%20busca%20em,j%C3%A1%20visitado%2C%20retornamos%20da%20busca.
    # busca em profundidade
    def dfs_recursiva(self, vertice, visitados, flag):
        visitados.add(vertice)
        falta_visitar = [vertice]
        for vizinho in self.retornaVizinhos(vertice-1):
            if vizinho not in visitados:
                visitados.add(vizinho)
                falta_visitar.append(vizinho)
                self.dfs_recursiva(vizinho, visitados,flag)
            else:
                """
                seleciona todos os pais e pais dos pais daquele vértice para 
                verificar se seu vizinho está ali incluso                
                """
                pais = self.retornaPais(vertice)
                for pai in pais:
                    paisDosPais = self.retornaPais(pai)
                    for paiDosPais in paisDosPais:
                        if(paiDosPais not in pais):
                            pais.append(paiDosPais)
                for pai in pais:
                    if(pai == vizinho):
                        flag[0] = True

    def retornaPais(self, v):   # retorna todos os pais de um vertice
        pais = []
        for i in range(len(self.matriz)):
                vizinhos = self.retornaVizinhos(i-1)
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