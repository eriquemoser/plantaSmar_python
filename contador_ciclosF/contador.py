from time import sleep
from contador_ciclosF.lib.interface import *
from contador_ciclosF.lib.arquivo import *

#arquivo que contém o diagnosticador reescrito
arq = 'diagnosticador_reescrito.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado!!!')
else:
    print('Arquivo não encontrado :(')
    criararquivo(arq)


while True:
    resposta = menu(['Iniciar contagem do número de estados', 'Sair do sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('Saindo do sistema... até logo')
        break
    else:
        print('\033[31mERRO, opção inválida. Tente novamente.\033[m')
    sleep(1)


