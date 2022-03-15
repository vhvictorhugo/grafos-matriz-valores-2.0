class Elemento(object):
    def __init__(self):
        self.vertice = 0
        self.proximo = 0
        self.marcado = False

class Grafo(object):
    def __init__(self):  # inicializa as estruturas base do grafo
        self.matriz = []

    def inicializaMatriz(self, n):  # inicializa a matriz de valores com 0
        posicao = [0, 0]    # por default, uma posicao recebe peso 0 e valor 0 para direcao de arco, sendo:
        for i in range(n):  # 1: se o arco tem origem no vértice i, -1: se i é o vértice destino do arco e 0: se nao há arco para o vértice i
            self.matriz.append([posicao] * n)

    def mostraMatriz(self):
        for linha in self.matriz:
            print(linha,"\n")

    def atribuiPosicao(self, linha, coluna, peso):  # atribui os pesos e direções dos arcos na matriz

        self.matriz[linha - 1][coluna - 1] = [peso, +1]
        self.matriz[coluna - 1][linha - 1] = [peso, -1]
        
    def retornaVizinhos(self, vertice): # percorre a coluna correspondente ao vértice e verifica os vizinhos
        vizinhos = []
        for i in range(len(self.matriz)):
            if self.matriz[vertice - 1][i][0] != 0:
                vizinhos.append(i + 1)
        return vizinhos

    # TESTAR

    # def ordem(self):  # ordem = nº de vértices
    #     ordem = len(self.matriz)    # nº de colunas ou nº de linhas da matriz

    #     return ordem

    # def tamanho(self):  # tamanho = nº de arestas
    #     tamanho = 0

    #     for i in range(len(self.matriz)):
    #         for j in range(len(self.matriz)):
    #             if (self.matriz[i][j] != 0):
    #                 tamanho += 1
    #     # sabemos que a matriz contém o mesmo peso 2x, uma em cada linha dos vértices ligados, logo, 
    #     # basta dividir tamanho por 2, para obter a quantidade de arestas
    #     tamanho = (tamanho / 2)

    #     return int(tamanho)

    # def listarVertices(self):
    #     vertices = []
    #     for i in range(len(self.matriz)):
    #         vertices.append(i+1)
    #     return vertices

    # def retornaVizinhos(self, vertice): # percorre a coluna correspondente ao vértice e verifica os vizinhos
    #     vizinhos = []
    #     for i in range(len(self.matriz)):
    #         if self.matriz[vertice - 1][i] != 0:
    #             vizinhos.append(i + 1)
    #     return vizinhos

    # def grauVertice(self, vertice): # percorre a coluna correspondente ao vértice e conta os vizinhos
    #     grau = 0
    #     for i in range(len(self.matriz)):
    #         if self.matriz[vertice - 1][i] != 0:
    #             grau += 1
    #     return grau


    # Fonte: https://pt.stackoverflow.com/questions/227717/como-utilizar-o-algoritmo-de-verifica%C3%A7%C3%A3o-de-ciclo-em-grafos

    def verificaCiclos(self, nodo_inicial):
        nodos_visitados = []
        nodos_restantes = [nodo_inicial]

        while nodos_restantes:
            nodo_atual = nodos_restantes.pop()
            nodos_visitados.append(nodo_atual)

            for vizinho in self.retornaVizinhos(nodo_atual):
                if vizinho in nodos_visitados:
                    return True

                nodos_restantes.append(vizinho)
        
        return False


grafo = Grafo()
nomeArquivo = "grafo.txt"
arquivo = open(f'.\\src\\{nomeArquivo}', 'r')

n = int(arquivo.readline())   

grafo.inicializaMatriz(n)

for linha in arquivo:
    linha = linha.split(' ')
    grafo.atribuiPosicao((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))
arquivo.close()

print(grafo.verificaCiclos(1))


    

    # 