from nbformat import read


class Elemento(object):
    def __init__(self):
        self.vertice = 0
        self.proximo = 0
        self.marcado = False

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
    
    # Cria uma copia da matriz e uma lista de vertices, chama a verificacao
    def verificaCiclo(self):
        vertices = []
        matriztemp = []
        contFalsos = 0  # conta a quantidade de verificacoes falsas para ciclos
        for i in range(len(self.matriz)):
            vertices.append(Elemento())
            vertices[i].vertice = i + 1
        for i in range(len(self.matriz)):
            matriztemp.append([0, 0] * len(self.matriz))
            for j in range(len(self.matriz)):
                matriztemp[i][j] = (self.matriz[i][j])
        # faz a verificacao para cada vertice i (grafos desconexos)
        for i in range(len(self.matriz)):
            if (self.verificacao(vertices, i, matriztemp) == False):
                contFalsos += 1
            else:
                return True
        
        return False

    # Verifica se possui um ciclo, marcando vertices e excluindo arestas ja visitadas.
    def verificacao(self, vertices, v, matriztemp):
        if vertices[v].marcado:
            return True
        else:
            for i in range(len(self.matriz)):
                if (matriztemp[v][i][0] != 0) and (matriztemp[v][i][1] != -1):
                    vertices[v].marcado = True
                    matriztemp[v][i][0] = 0
                    matriztemp[i][v][0] = 0
                    vertices[v].proximo = i + 1
                    return self.verificacao(vertices, i, matriztemp)
        return False

    def grauInterno(self, vertice):        
        grau = 0
        for i in range(len(self.matriz)):
            valorOrientacao = self.matriz[vertice][i][1]
            if(valorOrientacao == -1):  # codigo contendo uma matriz temporaria, a fim de recalcular o grau a cada alteracao no grafo
                grau += 1
        return grau

    def ordenacao_topologica(self):
        # Ordenação topológica baseada no grau de entrada dos vértices
        ordem_topologica = []

        # Calcula graus de entrada.
        graus_entrada = [0 for _ in range(len(self.matriz))]
        for vertice in self.matriz:
            listaVizinhos = self.retornaVizinhos(vertice)
            print(listaVizinhos)
            input("")
            for vizinho in listaVizinhos:
                graus_entrada[vizinho] += 1
        # Cria uma fila de vértices com grau de entrada zero.
        fila = [v for v in range(len(self.matriz)) if graus_entrada[v] == 0]
        while fila:
            vertice = fila.pop()
            ordem_topologica.append(vertice)
            # Atualiza o grau de entrada dos vizinhos.
            for vizinho in self.matriz[vertice]:
                graus_entrada[vizinho] -= 1
                # Algum dos vizinhos passou a ter grau de entrada zero.
                if graus_entrada[vizinho] == 0:
                    fila.append(vizinho)
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
grafo.mostraMatriz()
print(grafo.ordenacao_topologica())