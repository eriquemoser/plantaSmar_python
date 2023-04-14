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
def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possível ler o arquivo')
    else:
        cabecalho('VARREDURA:')
        contSX = 0
        nroF = 0
        for linha in a:
            dado = linha.split()
            contSX += 1

            if len(dado) == 1:
                if len(dado) != 0:
                    dado2 = dado[0].split(',')
                FlagSX = False
                for c in range(0, len(dado2)):
                    estado = dado2[c]
                    if estado[len(estado) - 1] == 'N':
                        FlagSX = True
                if FlagSX == True:
                    print("\033[31mEstado analisado:\033[m")
                    print(f'O estado {dado2} vale a pena analisar')
                    flagF = funceventos(nome, contSX)
                    nroF += flagF
        cabecalho('RESULTADO:')
        print(f'\033[032m EXISTEM {nroF} ESTADOS QUE LEVAM A FALHA !\033[m')
        print('')
    finally:
        a.close()


def funceventos(nome, contSX):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possível ler o arquivo')
    else:
        cont = 0
        flagF = 0
        for linha in a:
            dado = linha.split()
            cont += 1
            if cont > contSX:
                if len(dado) == 0:
                    break
                else:
                    dado2 = dado[1].split(',')
                    FlagSY = True
                    for c in range(0, len(dado2)):
                        estado = dado2[c]
                        if estado[len(estado) - 1] == 'N':
                            FlagSY = False
                    if FlagSY == True:
                        print("\033[32mEstado de falha encontrado:\033[m")
                        print(f'O estado {dado2} tem falha')
                        flagF = 1

        return flagF

    finally:
        a.close()
################
