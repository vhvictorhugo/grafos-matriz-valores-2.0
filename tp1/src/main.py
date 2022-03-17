import grafoDirigido
import grafo
import os

def printMenu():
    print("_"* 60)
    print(3*"\t","MENU")
    print("_"* 60)
def inicializar(grafoNaoDirigido, grafoOrientado, tipoEntrada):

    if tipoEntrada == 1:
        nomeArquivo = input("Digite o nome do arquivo Json: ")
        grafoNaoDirigido.lerJson(nomeArquivo)
        nomeArquivo = nomeArquivo.replace("json","txt")
    else:
        nomeArquivo = input("Digite o nome do arquivo txt: ")


    arquivo = open(f'arquivos\\{nomeArquivo}', 'r')

    n = int(arquivo.readline())

    print("_"* 60)
    print("Escolha o tipo do grafo:\n1) Orientado\n2) Não orientado")
    escolha = int(input())
    if(escolha == 1):
        grafoOrientado.inicializaMatriz(n)
        for linha in arquivo:
            linha = linha.split(' ')
            grafoOrientado.atribuiPosicao((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))
        arquivo.close()
        print("Grafo Orientado inicializado") 
    elif(escolha == 2):
        grafoNaoDirigido.inicializaMatriz(n)
        for linha in arquivo:
            linha = linha.split(' ')
            grafoNaoDirigido.atribuiPeso((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))
        arquivo.close()
        print("Grafo Não Orientado inicializado") 

def escolherArquivo(grafoNaoDirigido, grafoOrientado):
    print("_"* 60)
    print(3*"\t","MENU")
    print("_"* 60)
    print("Escolha o formato da entrada de arquivo:\n1) Json\n2) txt")
    tipo = int(input("->"))
    inicializar(grafoNaoDirigido, grafoOrientado, tipo)

def menuFuncoes():
    while True:
        printMenu()
        print("1) Ordem do grafo")
        print("2) Tamanho do grafo")
        print("3) Densidade")
        print("4) Vizinho de um vertice")
        print("5) Grau de um vertice")
        print("6) Verificar se um vertice e articulacao")
        print("7) Busca em Largura")
        print("8) Numero de componentes conexas do grafo e os vértices de cada componente")
        print("9) Verificar se possui ciclo")
        print("10) Distancia e caminho minimo ")
        print("11) A árvore geradora mínima de um grafo ")
        print("12) Verificar se um grafo é euleriano ")
        print("13) Conjunto independente")
        print("14) Numero cromatico")
        print("0) Sair")
        
        escolha = int(input("->"))

        if grafoNaoDirigido == None: 
            print("Primeiro Inicialize o Grafo")
         
           
        elif escolha == 1:
            print("Ordem do grafo: ",grafoNaoDirigido.ordem())
      

        elif escolha == 2:
            print("Tamanho do grafo: ",grafoNaoDirigido.tamanho())
     
        elif escolha == 3:
            print("A desidade do grafo e ",grafoNaoDirigido.densidade())
              
        elif escolha == 4:
            vertice = int(input("Escolha um verticer para saber seu vizinhos:\n->"))
            print("Vizinho de um vertice:",grafoNaoDirigido.retornaVizinhos(vertice))
              
        elif escolha == 5:
            vertice = int(input("Escolha um vertice:\n->"))
            print("Vertice de grau:",grafoNaoDirigido.grauVertice(vertice))
             
        elif escolha == 6:
            vertice = int(input("Escolha um vertice pra comecar:\n->"))
            print("O vertice e articulacao") if grafoNaoDirigido.articulacao(vertice) else print("O vertice nao e articulacao") 
                          
        elif escolha == 7:
            vertice = int(input("Escolha um vertice pra comecar:\n->"))
            print("busca em largura:")
            grafoNaoDirigido.buscaEmLargura(vertice)

        elif escolha == 8:
            print("Numero de componentes conexas: ", grafoNaoDirigido.componentesConexas(grafoNaoDirigido.ordem())[0])
            print("Vertices de cada componente:\n")
            grafoNaoDirigido.mostraVerticesComponente(grafoNaoDirigido.componentesConexas(grafoNaoDirigido.ordem())[1])
           

        elif escolha == 9:
            print("O Grafo possui ciclo") if grafoNaoDirigido.verificaCiclo() else print("O Grafo nao possui ciclo")

        elif escolha == 10:
            vertice = int(input("Escolha um vertice pra comecar:\n->"))
            grafoNaoDirigido.menorCaminhoVertice(vertice)            
        
        elif escolha == 11:
            printArvoreMinima()
            
        elif escolha == 12:
            grafoNaoDirigido.verificarEuliriano()       

        elif escolha == 13:
            print("Conjunto independente:", grafoNaoDirigido.heuristicaGulosa()[1])
        
        elif escolha == 14:
            print("Numero cromatico do grafo é :", grafoNaoDirigido.numeroCromatico())
        else:
            break
def printArvoreMinima():
    n=grafoNaoDirigido.ordem()
    verificaComponentesConexas = False  # false: grafo possui mais de 1 componente conexa

    if grafoNaoDirigido.componentesConexas(n)[0] > 1:
        verificaComponentesConexas = True   # grafo possui mais de 1 componente,

    if verificaComponentesConexas != True:
        n=grafoNaoDirigido.ordem()
        mst = grafoNaoDirigido.primMST(n)
        # Criando e escrevendo em arquivos de texto (modo 'w'). escrita
        arquivo = open('arq01.txt','w')

        arquivo.write(str (n) + '\n')

        for i in range(1, n):
            aresta1, aresta2, peso = grafoNaoDirigido.getParams(mst, i)
            arquivo.write(str (aresta1) + ' ' + str (aresta2) + ' ' + str (peso) + '\n')
        arquivo.close()
    else:
        print("Grafo desconexo, logo nao eh possivel!")
def menuDirigido():
    visitados = set() # Set to keep track of visited nodes of graph
    """
    aqui iremos explorar o conceito de referencia na linguagem Python:
        quando criamos uma lista, como no caso de 'vetorSolucao', e a atribuimos a outra variavel,
        como em parâmetros de funções ou até mesmo uma simples atribuição, se não criarmos uma cópia
        é passada sua referência e portanto, você estará utilizando aquela mesma lista
    """
    vetorSolucao = [False]  # indica que não há ciclos no
    """
    passamos esta lista por referência em 'def_recursiva', pois é esta lista que 
    queremos alterar ao longo das chamadas recursivas
    caso seja encontrado um arco de retorno na busca em profundidade esta lista de 1 
    posição é alterada de '[False]' para '[True]'
    """
    #print(grafo.dfs_recursiva(0,visitados,vetorSolucao))
    grafoOrientado.dfs_recursiva(0,visitados,vetorSolucao)   # efetua a chamada para obter a solucao em 'vetorSolucao'
    if(vetorSolucao[0] == False):
        print("Grafo Acíclico!")
        print("Ordenacao Topologica:", grafoOrientado.ordenacao_topologica())
    else:
        print("Grafo Cíclico, não é possível fazer a ordenação topológica!")

grafoNaoDirigido = None
grafoOrientado = None
while True:
    printMenu()
    print("1) Escolher o arquivo")
    print("2) Biblioteca (Grafos Não Direcionados)")
    print("3) Verificar se Grafo Direcionado é Acíclico")
    print("4) Converter o grafo para Json(Grafo Não Direcionado)")
    print("0) Sair")
    escolha = int(input("->"))
    if escolha == 1:
        grafoNaoDirigido = grafo.Grafo()
        grafoOrientado = grafoDirigido.GrafoDirigido()
        escolherArquivo(grafoNaoDirigido, grafoOrientado)

    if escolha == 2:
        if grafoNaoDirigido == None: 
            print("Primeiro Inicialize o Grafo")
        else:
            menuFuncoes()

    if escolha == 3:
        if(grafoOrientado == None):
            print("Primeiro Inicialize o Grafo")
        else:
            menuDirigido()

    if escolha == 4:
        if grafoNaoDirigido == None: 
            print("Primeiro Inicialize o Grafo")
        else:
            grafoNaoDirigido.escreverJson()
            

    if escolha == 0:
            break   