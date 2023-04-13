from contador_ciclosF.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve problema na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')

################
def lerarquivo(nome, eventos, pos):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possível ler o arquivo')
    else:
        cabecalho('EVENTOS DISPONÍVEIS:')
        for linha in a:
            dado = linha.split(' ')
            dado[2] = dado[2].replace('\n', '')
            if dado[0] == str(pos):
                lereventos(eventos,dado[1])
            # print(dado)
            # print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def lereventos(arquivo,num):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Não foi possível abrir esse arquivo')
    else:
        for linha in a:
            dado = linha.split(' ')
            dado[1] = dado[1].replace('\n', '')
            #print(dado)
            if dado[0] == str(num):
                print(f'{num} - {dado[1]}')

#teste
###############
def evoluir(arquivo, pos, evento):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Não foi possível abrir esse arquivo')
    else:
        for linha in a:
            dado = linha.split(' ')
            dado[2] = dado[2].replace('\n', '')
            if dado[0] == str(pos):
                if dado[1] == str(evento):
                    #print('bingo!')
                    post = dado[2]
    return post