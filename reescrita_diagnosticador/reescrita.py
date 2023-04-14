from time import sleep
from reescrita_diagnosticador.lib.interface import *
from reescrita_diagnosticador.lib.arquivo import *

#arquivos analisados
arq = 'exemplosmar.txt'
novoarquivo = 'novo.txt' #esse txt deve sempre apagar o conteúdo dentro antes de uma nova varredura

if arquivoExiste(arq):
    print('Arquivo encontrado!!!')
else:
    print('Arquivo não encontrado :(')
    criararquivo(arq)

while True:
    resposta = menu(['Iniciar procedimento de conversão do diagnosticador (limpar conteúdo de "novo.txt"', 'Sair do sistema'])
    if resposta == 1:
        lerarquivo(arq,novoarquivo)
    elif resposta == 2:
        cabecalho('Saindo do sistema... até logo')
        break
    else:
        print('\033[31mERRO, opção inválida. Tente novamente.\033[m')
    sleep(1)



