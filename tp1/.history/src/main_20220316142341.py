import grafoDirigido
import grafo
import os

def printMenu():
    print("_"* 60)
    print(3*"\t","MENU")
    print("_"* 60)
def inicializar(grafoNaoDirigido, grafoDirigido, tipoEntrada):

    if tipoEntrada == 1:
        nomeArquivo = input("Digite o nome do arquivo Json: ")
        grafoNaoDirigido.lerJson(nomeArquivo)
        nomeArquivo = nomeArquivo.replace("json","txt")
    else:
        nomeArquivo = input("Digite o nome do arquivo txt: ")

    arquivo = open(f'C:\\Users\\victo\\Documents\\MEGAsync\\Faculdade\\PHT\\Grafos\\TPs\\2\\tp1\\arquivos\\{nomeArquivo}', 'r')

    n = int(arquivo.readline())

    print("_"* 60)
    escolha = int(input("Escolha o tipo do grafo:\n1) Orientado\n2) Não orientado"))
    if(escolha == 1):
        grafoDirigido.inicializaMatriz(n)
        for linha in arquivo:
            linha = linha.split(' ')
            grafo.atribuiPosicao((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))
        arquivo.close()
        print("Grafo inicializado") 
    elif(escolha == 2):
        grafoNaoDirigido.inicializaMatriz(n)
        for linha in arquivo:
            linha = linha.split(' ')
            grafoNaoDirigido.atribuiPeso((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))
        arquivo.close()
        print("Grafo inicializado") 

def escolherArquivo(grafoNaoDirigido, grafoDirigido):
    print("_"* 60)
    print(3*"\t","MENU")
    print("_"* 60)
    print("Escolha o formato da entrada de arquivo:\n1) Json\n2) txt")
    tipo = int(input("->"))
    inicializar(grafoNaoDirigido, grafoDirigido, tipo)

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
            print("Conjunto de independencia:", grafoNaoDirigido.heuristicaGulosa()[1])
        
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
# def menuDirigido():
grafoNaoDirigido = None
grafoDirigido = None
while True:
    printMenu()
    print("1) Escolher o arquivo")
    print("2) Usar as funcoes do grafo (grafo não dirigido)")
    print("3) Usar grafo dirigido")
    print("4) Converter o grafo para Json")
    print("0) Sair")
    escolha = int(input("->"))
    if escolha == 1:
        grafoNaoDirigido = grafo.Grafo()
        #grafoDirigido = grafoDirigido.GrafoDirigido()
        escolherArquivo(grafoNaoDirigido, grafoDirigido)

    if escolha == 2:
        if grafoNaoDirigido == None: 
            print("Primeiro Inicialize o Grafo")
        else:
            menuFuncoes()

    if escolha == 3:
        if(grafoDirigido == None):
            print("Primeiro Inicialize o Grafo")
        #else:
            #menuDirigido()

    if escolha == 4:
        if grafoNaoDirigido == None: 
            print("Primeiro Inicialize o Grafo")
        else:
            grafoNaoDirigido.escreverJson()
            

    if escolha == 0:
            break   