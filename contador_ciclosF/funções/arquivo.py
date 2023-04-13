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
        cabecalho('VARREDURA:')
        contSX=0
        for linha in a:
            dado = linha.split()
            contSX+=1
            if len(dado) == 1:
                estadosx=str(dado[0])
                #imprime os valores que tem N e F
                if 'N' in estadosx or ('N' in estadosx and 'F' in estadosx):
                    print("Estado analisado:")
                    print(estadosx)
                    funceventos(nome,estadosx,contSX)
            #if len(dado) == 0:
                #valid_answer=0

    finally:
        a.close()

def funceventos(nome,estadosx,contSX):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possível ler o arquivo')
    else:
        #cabecalho('entrei:')
        print('transições:')
        cont=0
        for linha in a:
            dado = linha.split()
            cont+=1
            if cont > contSX:
                if len(dado) == 0:
                    break
                else:
                    print(dado)

    finally:
        a.close()
################

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