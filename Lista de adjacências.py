
index=999
eventos = ["a", "b", "c"]
grafo = [[['a',3],['b',1]],['a',2],['c',0],['b',2]]
#print(grafo[0])
pos = 3

#print(grafo[pos])
while True:

    var = str(input('Digite o evento [0 p/ parar]: '))
    if var == '0':
        break
    for elemento in grafo[pos]:

        if type(elemento) == list:
            if var in elemento:
                #index = elemento.index(var)
                print(elemento[1])
                pos = elemento[1]
                break
        else:
            if var in grafo[pos]:
                print(grafo[pos][1])
                pos = grafo[pos][1]
    print(grafo)


#print(index)
#print(pos)

#while True:
#    a=input("Digite o evento: ")
#    if a