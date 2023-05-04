from time import sleep
from testee.lib.interface import *
from testee.lib.arquivo import *

arq = 'diagsimplificado.txt'
eventos = 'eventos.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado!!!')
else:
    print('Arquivo não encontrado :(')
    criararquivo(arq)

pos = 0

while True:
    resposta = menu(['Ver eventos disponíveis', 'Digitar novo evento', 'Sair do sistema'],pos)
    if resposta == 1:
        lerarquivo(arq, eventos, pos)
    elif resposta == 2:
        cabecalho('NOVO EVENTO')
        evento = int(input('Digite o número do evento: '))
        post=evoluir(arq,pos,evento)
        pos=post
    elif resposta == 3:
        cabecalho('Saindo do sistema... até logo')
        break
    else:
        print('\033[31mERRO, opção inválida. Tente novamente.\033[m')
    sleep(1)


