# https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/representacao-grafos/
import json
from tkinter import N
import sys
from operator import itemgetter, attrgetter

class Elemento(object):
    def __init__(self):
        self.vertice = 0
        self.proximo = 0
        self.marcado = False


class Grafo(object):
    def __init__(self):  # inicializa as estruturas base do grafo
        self.matriz = []

    def inicializaMatriz(self, n):  # inicializa a matriz de valores com 0
        for i in range(n):
            self.matriz.append([0] * n)

    def atribuiPeso(self, linha, coluna, peso):  # atribui os pesos das arestas na matriz

        self.matriz[linha - 1][coluna - 1] = peso
        self.matriz[coluna - 1][linha - 1] = peso

    def ordem(self):  # ordem = nº de vértices
        ordem = len(self.matriz)    # nº de colunas ou nº de linhas da matriz

        return ordem

    def tamanho(self):  # tamanho = nº de arestas
        tamanho = 0

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if (self.matriz[i][j] != 0):
                    tamanho += 1
        # sabemos que a matriz contém o mesmo peso 2x, uma em cada linha dos vértices ligados, logo, 
        # basta dividir tamanho por 2, para obter a quantidade de arestas
        tamanho = (tamanho / 2)

        return int(tamanho)

    def densidade(self):
        return self.tamanho() / self.ordem()  # Densidade = numero de arestas / numero de vertices (|M|/|N|)

    def retornaVizinhos(self, vertice): # percorre a coluna correspondente ao vértice e verifica os vizinhos
        vizinhos = []
        for i in range(len(self.matriz)):
            if self.matriz[vertice - 1][i] != 0:
                vizinhos.append(i + 1)
        return vizinhos

    def grauVertice(self, vertice): # percorre a coluna correspondente ao vértice e conta os vizinhos
        grau = 0
        for i in range(len(self.matriz)):
            if self.matriz[vertice - 1][i] != 0:
                grau += 1
        return grau
    
    # funcao auxiliar para articulacao()
    # "Marca" todos os vertices que podem ser acessados apartir de um vertice "v"
    def busca(self, vertice, marcados=[], verticeRetirado=None):

        if (verticeRetirado):
            marcados.append(verticeRetirado)

        marcados.append(vertice)
        for vizinho in self.retornaVizinhos(vertice):
            if vizinho not in marcados:
                self.busca(vizinho, marcados)

    # Verifica se um vertice é articulação
    def articulacao(self, vertice):
        if vertice not in self.matriz:
            return False
        for vizinho in self.retornaVizinhos(vertice):
            comVertice = []
            semVertice = []
            self.busca(vizinho, comVertice)
            self.busca(vizinho, semVertice, vertice)
            comVertice.sort()
            semVertice.sort()
            if (comVertice != semVertice):  # compara se ouve alguma mudança nos vertices marcados
                return True
        return False

    def buscaEmLargura(self, vertice):
        fila = []
        marcados = []
        i = 1

        fila.append(vertice)
        marcados.append(vertice)
       
        matrizArestas = [[0] * len(self.matriz) for _ in range(len(self.matriz))]
        foraDaBusca = [[0] * len(self.matriz) for _ in range(len(self.matriz))]
       
        while len(fila) > 0:
            v = fila[0]
            vizinhos = self.retornaVizinhos(v)
            
            for w in vizinhos:
                if w not in marcados: #se o vertice não foi explorado, o adiciona na fila para ser explorado
                    matrizArestas[v - 1][w - 1] = 1  # adiciona as arestas na árvore de busca em largura
                    matrizArestas[w - 1][v - 1] = 1
                    marcados.append(w)
                    fila.append(w)
                elif w in fila:
                    foraDaBusca[v-1][w-1] = 1
            fila.remove(v)             #remove o vertice explorado da fila

        print("Ordem de vizitacao dos vertices na busca em largura:")
        for vertice in marcados:
            print(' ->',vertice, end= '')
        print()

        print("Arestas que nao fazem parte da busca em largura:")
        for i in range(len(foraDaBusca)):
            for j in range(len(foraDaBusca)):
                if foraDaBusca[i][j] == 1:
                    print(f"Aresta {i+1} {j+1}")

    # funcao auxiliar para componentesConexas
    def find(self, n1, pais = []): # encontra a qual componente o i-ésimo nó pertence

        componente = n1
        
        while(componente != pais[componente]):
            pais[componente] = pais[pais[componente]]
            componente = pais[componente]
        return componente

    # funcao auxiliar para componentesConexas()
    def union(self, n1, n2, pais = [], tamanhoComponente = []): # faz a união entre as componentes
        p1, p2 = self.find(n1, pais), self.find(n2, pais)

        if p1 == p2: # nao sera feita a uniao, pois ja pertencem a mesma componente
            return 0
        
        if (tamanhoComponente[p2] > tamanhoComponente[p1]): # sera feita a uniao, pois nao pertencem a mesma componente
            pais[p1] = p2
            tamanhoComponente[p2] += tamanhoComponente[p1]
        else:  # sera feita a uniao também
            pais[p2] = p1
            tamanhoComponente[p1] += tamanhoComponente[p2]
        
        return 1

    # funcao auxiliar para componentesConexas()
    def mostraVerticesComponente(self, pais):
        for i in range (len(pais)):
            print("Componente do vértice ", i+1,": ", pais[i])
 
    def componentesConexas(self, n): # retorna a quantidade de componentes conexas e também a componente conexa de um determinado vértice i pelo array 'pais'
        # este código é uma adaptação do algoritmo Union Find disponibilizado pelo canal NeetCode no youtube; 
        # Link: https://www.youtube.com/watch?v=8f1XPm4WOUc&t

        # Este algoritmo seleciona 'edge by edge' (aresta a aresta), qual a componente
        # conexa que aquele determinado vértice pertence por meio de 1 vértice identificador
        
        pais = [i for i in range(n)]
        tamanhoComponente = [1] * n

        quantidadeComponentes = n
        
        for i in range(n):
            for j in range(n):
                if (self.matriz[i][j] != 0):
                    quantidadeComponentes -= self.union(i, j, pais, tamanhoComponente)

        return quantidadeComponentes, pais

    # Cria uma copia da matriz de adjacencia e uma lista de vertices, chama a verificacao
    def verificaCiclo(self):
        vertices = []
        matriztemp = []
        for i in range(len(self.matriz)):
            vertices.append(Elemento())
            vertices[i].vertice = i + 1
        for i in range(len(self.matriz)):
            matriztemp.append([0] * len(self.matriz))
            for j in range(len(self.matriz)):
                matriztemp[i][j] = (self.matriz[i][j])
        return self.verificacao(vertices, 0, matriztemp)

    # Verifica se possui um ciclo, marcando vertices e excluindo arestas ja visitadas.
    def verificacao(self, vertices, v, matriztemp):
        if vertices[v].marcado:
            return True
        else:
            for i in range(len(self.matriz)):
                if matriztemp[v][i] != 0:
                    vertices[v].marcado = True
                    matriztemp[v][i] = 0
                    matriztemp[i][v] = 0
                    vertices[v].proximo = i + 1
                    return self.verificacao(vertices, i, matriztemp)
        return False

    # Algoritmo de Floyd-Warshall (Aplicado a grafos com ciclos positivos)
    def menorCaminhoVertice(self, v):
        matrizL = []
        matrizR = []
        infinito = float("inf")
        n = len(self.matriz)
        # Inicialização matriz L e R
        for i in range(n):
            matrizL.append([infinito] * n)
            matrizR.append([0] * n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrizL[i][j] = 0
                else:
                    if self.matriz[i][j] != 0:
                        matrizL[i][j] = self.matriz[i][j]
        for i in range(n):
            for j in range(n):
                if matrizL[i][j] != infinito:
                    matrizR[i][j] = i + 1
        # Calculo Menor Caminho
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrizL[i][j] > matrizL[i][k] + matrizL[k][j]:
                        matrizL[i][j] = matrizL[i][k] + matrizL[k][j]
                        matrizR[i][j] = matrizR[k][j]
        self.imprimeDistancia(matrizL[v - 1], v)
        for i in range(n):
            self.imprimeCaminhoMinimo(matrizR[v - 1], v, i + 1)

    def imprimeDistancia(self, vetorDistancia, v):
        for i in range(len(vetorDistancia)):
            print("Distância entre o vertice", v, "e", i + 1, "=", round(vetorDistancia[i], 2))

    def imprimeCaminhoMinimo(self, vetorCaminho, v1, v2):
        temp = []
        vnext = v2
        for i in range(len(vetorCaminho)):
            temp.append(vnext)
            if vetorCaminho[vnext - 1] == 0:
                print(v1)
                return
            elif vetorCaminho[vnext - 1] != v1:
                vnext = vetorCaminho[vnext - 1]
            else:
                break
        temp.append(v1)
        temp.reverse()
        print("Caminho Minimo entre", v1, "e", v2, ":")
        for vertice in temp:
            print(" ->", vertice, end="")
        print("")
    

        
    def verificarEuliriano(self):
        #verificar se o grafo tem todos os vertices com grau par
        for i in range(len(self.matriz)):
            if self.grauVertice(i) % 2 == 1:
                print("Grafo nao e euliriano vertice", i+1)
                return False

        #verificar se o grafo é conexo
        conexo = []
        self.busca(1, conexo)
        if len(conexo) != len(self.matriz):
            print("Grafo nao e euliriano")
            return False
        #Se passou dos testes o grafo é euliriano
        print("Grafo e euliriano")

        copia = [[] * len(self.matriz) for _ in range(len(self.matriz))]
        for i in range(len(self.matriz)):
            copia[i] = self.matriz[i].copy()
        #determinar uma cadeia euliriana fechada com o algoritmo de Fleury
        self.cadeiaEuliriana()
        
    def cadeiaEuliriana(self):

        v0 = 1
        cadeia = [v0] #cadeia inicia num vertice qualquer

        matriz = [[] * len(self.matriz) for _ in range(len(self.matriz))]
        for i in range(len(self.matriz)):
            matriz[i] = self.matriz[i].copy()
        
        while True:
            vertice = cadeia[len(cadeia) -1] #vertice a ser explorado é o ultimo na cadeia
            arestasIncidentes = []

            for  i in range (len(matriz)):
                if (matriz[vertice-1][i] != 0):
                    arestasIncidentes.append(i) #arestas incidentes no vertice

            if (len(arestasIncidentes) == 0): #se não há mais arestas o algoritmo chegou ao fim
                break 

            if (len(arestasIncidentes) == 1): #se há somente uma aresta é ela que vamos atravessar
                aresta = arestasIncidentes[0]

            else:
                pos = 1
               
                for j in arestasIncidentes: #para cada aresta incidente no vertice
                    cont = 0
                    if pos == len(arestasIncidentes): #se é a ultima aresta no vetor de arestas inicidentes +
                        aresta = j                    # então as outras são ponte, escolheremos essa para atravessar
                    else:
                        for aresta in matriz[j]:      #conta a quantidade de arestas incidentes no vertice ligado ao +                                                                   
                            if aresta != 0:           # vertice atual pela aresta atual.
                                cont +=1
                        if (cont > 1):                #se há mais de uma aresta, a aresta atual não é uma ponte
                            aresta = j
                            break
                        pos += 1
            matriz[vertice-1][aresta] = 0            #Marca a aresta como explorada
            matriz[aresta][vertice-1] = 0            #Marca a aresta como explorada
            cadeia.append(aresta+1)

        print("Cadeia euliriana no grafo: ", cadeia)

    def escreverJson(self):
        with open(".\\src\\base.json", encoding='utf-8') as meu_json:
            j = json.load(meu_json)
        
    
        for v in range (len(self.matriz)):
            vertice = {
                    "id": v+1,
                    "x": 45,
                    "y": 45,
                    "label": f"{v+1}"
            }
            j["data"]["nodes"]["_data"][f"{v+1}"] = vertice

        j["data"]["nodes"]["length"] = f"{len(self.matriz)}"

        id = 1

        matriz = [[] * len(self.matriz) for _ in range(len(self.matriz))]
        for i in range(len(self.matriz)):
            matriz[i] = self.matriz[i].copy()

        for i in range (len(matriz)):
            for x in range (len(matriz)): 
                if(matriz[i][x] != 0):

                    aresta = { 
                                "from": f"{i+1}",
                                "to": f"{x+1}",
                                "label": f"{matriz[i][x]}",
                                "id": f"{id}",
                                "color": {}
                            }   
                    matriz[i][x]  = 0
                    matriz[x][i]  = 0            
                    j["data"]["edges"]["_data"][f"{id}"] = aresta
                    id += 1

            
        with open('data.json', 'w+') as f:
            json.dump(j, f)
        print("Arquivo convertido, o nome do arquivo e data.json")

    

    def lerJson(self, nomeArquivo):
        try:
            with open(f".\\src\\{nomeArquivo}", encoding='utf-8') as meu_json:
                dados = json.load(meu_json)
        except:
            print("arquivo nao encontrado, verifique se esta na pasta src")
            

        nomeArquivo = nomeArquivo.replace("json","txt")
        try:
            arquivo = open(f".\\src\\{nomeArquivo}", "w+")
        except:
            print("Erro ao abrir o arquivo")

        arquivo.writelines(f"{ dados['data']['nodes']['length'] }\n")

        arestas = []
        for prop in dados["data"]["edges"]["_data"].values():
            arestas.append(prop)

        vertices = []
        for prop in dados["data"]["nodes"]["_data"].values():
            vertices.append(prop)
        for aresta in arestas:
            vertice1 = aresta['from'] if  aresta['from'] == vertices[aresta['from']-1]['label'] else vertices[aresta['from']-1]['label']
            vertice2 =  aresta['to'] if  aresta['to'] == vertices[aresta['to']-1]['label'] else vertices[aresta['to']-1]['label']
            peso = aresta['label']
            arquivo.writelines(f"{vertice1} {vertice2} {peso}\n")   


    def printMST(self, parent, n):
        print (n)
        for i in range(1, n):
            parentAux = parent[i]
            print (parentAux+1, " ", i+1, "\t", self.matriz[i][parentAux])

    def getParams(self, parent, i):

        aresta1 = parent[i]
        aresta2 = i
        peso = self.matriz[i][aresta1]

        return aresta1+1, aresta2+1, peso

    def minKey(self, key, mstSet, n):

        min = sys.maxsize

        min_index = 0
 
        for v in range(n):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    def primMST(self, n):
        ##tirado do sitehttps://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/ e adptado para o tp
        key = [sys.maxsize] * n
        parent = [None] * n
        key[0] = 0
        mstSet = [False] * n
 
        parent[0] = -1 
 
        for cout in range(n):
 
            u = self.minKey(key, mstSet, n)

            mstSet[u] = True

            for v in range(n):
 
                if self.matriz[u][v] > 0 and mstSet[v] == False and key[v] > self.matriz[u][v]:
                        key[v] = self.matriz[u][v]
                        parent[v] = u

        self.printMST(parent, n)

        return parent
        
    def listarVertices(self):
        vertices = []
        for i in range(len(self.matriz)):
            vertices.append(i+1)
        return vertices
        
    # heuristica gulosa para determinar um conjunto independente ou estável
    def heuristicaGulosa(self):
        S = []
        numeroIndependência = 0
        vertices = self.listarVertices().copy()    # nao esquecer que os vértices sao listados de acordo com sua representacao e a matriz começa em 0
        verticesEGraus = [] # lista auxiliar para salvar os vertices e seus respectivos graus
        print(vertices)
        for c in vertices:
            verticesEGraus.append([c, self.grauVertice(c)])
            
        # ordenando os vértices em ordem decrescente de graus
        verticesEGraus = sorted(verticesEGraus, key=itemgetter(1), reverse=True)
        print(vertices)
        print(verticesEGraus)

        #atribuindo ordenacao à lista vertices

        for i in range(len(verticesEGraus)):
            vertices = verticesEGraus[0]

        print(vertices)
        print(verticesEGraus)

        while (len(vertices) != 0):
            maiorGrau = verticesEGraus[0][0]
            # remocao do vertice de maior grau
            print(len(vertices))
            
            vertices.pop(vertices.index(verticesEGraus[0][0]))
            print(len(vertices))
            print(vertices)

            # remocao dos vizinhos do vertice de maior grau
