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

    def listarVertices(self):
        vertices = []
        for i in range(len(self.matriz)):
            vertices.append(i+1)
        return vertices
        
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

    
        
    
        
    # heuristica gulosa para determinar um conjunto independente ou estável
    def heuristicaGulosa(self):
        S = []
        numeroIndependência = 0
        vertices = []
        verticesEGraus = [] # lista auxiliar para salvar os vertices e seus respectivos graus
        
        # recuperando os vértices e seus respectivos graus
        for v in self.listarVertices().copy():
            verticesEGraus.append([v, self.grauVertice(v)])

        # ordenando os vértices em ordem decrescente de graus
        verticesEGraus = sorted(verticesEGraus, key=itemgetter(1), reverse=True)
            
        for v in verticesEGraus:
            vertices.append(v[0])
        
        while (len(vertices) > 0):
            # recupera vertice de maior grau
            maiorGrau = vertices[0]
            # remove vertice de maior grau
            vertices.pop(0)
            # remove vizinhos do vertice de maior grau
            for vizinho in self.retornaVizinhos(maiorGrau):
                if(vizinho not in vertices):
                    break
                indiceVizinho = vertices.index(vizinho)
                vertices.pop(indiceVizinho)

            S.append(maiorGrau)

            numeroIndependência += 1

        return numeroIndependência, S
