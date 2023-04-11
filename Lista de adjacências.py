def leitura(grafo):
    '''
    Função que recebe uma posição do grafo, então será exibido quais eventos estão habilitados
    :param grafo: posição atual do grafo
    :return: impressão dos eventos habilitados
    '''
    for p, v in enumerate(grafo):
        if type(v) == list:
            for q, u in enumerate(v):
                if q == 0:
                    print(u, end=' ')
                #print(var[0])
        else:
            if p == 0:
                print(v, end=' ')
    print('\n')

#grafo e posição inicial
grafo = [
    [['a',3],['b',1]],
    ['a',2],
    ['c',0],
    ['b',2]
]
pos = 3


#evolução do grafo de acordo com o evento informado pelo operador
while True:
    print(f'estado atual: {pos}')
    print('eventos habilitados: ', end = '')
    leitura(grafo[pos])
    #print(grafo[pos])
    var = str(input('Digite o evento desejado [0 p/ parar]: '))
    if var == '0':
        break
    for elemento in grafo[pos]:

        if type(elemento) == list:
            if var in elemento:
                #index = elemento.index(var)
                #print(elemento[1])
                pos = elemento[1]
                break
        else:
            if var in grafo[pos]:
                #print(grafo[pos][1])
                pos = grafo[pos][1]


