from reescrita_diagnosticador.lib.interface import *

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
def lerarquivo(nome,novoarquivo):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possível ler o arquivo')
    else:
        cabecalho('VARREDURA:')
        for p,linha in enumerate(a):
            dado = linha.split()
            if p > 1:
                print(len(dado))
                print(dado)
                if len(dado) == 3:
                    string=dado[0]
                    cadastrar(novoarquivo,string)
                if len(dado) == 4:
                    string = dado[0] + ' ' + dado[1]
                    cadastrar(novoarquivo, string)
                if len(dado) == 0:
                    cadastrar(novoarquivo, '')

    finally:
        a.close()

################

def cadastrar(arquivo,string):
    try:
        a = open(arquivo, 'at')
    except:
        print('Não foi possível abrir esse arquivo')
    else:
        try:
            a.write(f'{string}\n')
        except:
            print('Houve um problema na escrita do arquivo')
        else:
            print(f'ok!')
            a.close()