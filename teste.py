lista = ['S2Nome', 'ALEGRIA']
print(lista)
lista2 = lista[0].split(',')
nome = lista2[0]
#print(lista2[0])
#print(len(lista2[0]))
print(f'{nome[len(nome)-2]}{nome[len(nome)-1]}')
#print(lista[0][len(lista)-1]