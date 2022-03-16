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
            if (self.matriz[vertice - 1][i][0] != 0) and (self.matriz[vertice-1][i][1] == 1):
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

    def grauInterno(self, vertice, matrizTemporaria):        
        grau = 0
        for i in range(len(self.matriz)):
            # if(self.matriz[vertice][i][1] == -1): # codigo original
            if(matrizTemporaria[vertice][i][1] == -1):  # codigo contendo uma matriz temporaria, a fim de recalcular o grau a cada alteracao no grafo
                grau += 1
        return grau

    def ordenacaoTopologica(self):
        # verificaCiclo = self.verificaCiclo()
        # if (verificaCiclo == True):
        #     print("Grafo possui ciclo, nao e possivel efetuar a ordenacao topologica")
        #     return
        # else:
        matrizTemp = self.matriz
        R = []
        grausInternos = []
        while(len(R) != len(matrizTemp)):
            # recupera os graus internos dos vertices
            for i in range(len(matrizTemp)):
                grausInternos.append(self.grauInterno(i, matrizTemp))
                            
            print("graus internos:", grausInternos)

            R.append(grausInternos.index(0)+1)

            print(matrizTemp.index(grausInternos.item(0)))
            
            for i in range(len(matrizTemp)):
                for j in range(len(matrizTemp)):
                    if(i == grausInternos.index(0)):
                        matrizTemp[i][j][1] = 0

            grausInternos.clear()
            # print("graus internos:", grausInternos)  
        # print(R)
        return R

grafo = Grafo()
nomeArquivo = "grafo_t.txt"
arquivo = open(f'.\\src\\{nomeArquivo}', 'r')
n = int(arquivo.readline())
grafo.inicializaMatriz(n)
for linha in arquivo:
    linha = linha.split(' ')
    grafo.atribuiPosicao((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))
arquivo.close()

for i in range(len(grafo.matriz)):
    print(grafo.matriz[i])

# print("Grafo possui ciclo?", grafo.verificaCiclo())
print(grafo.ordenacaoTopologica())