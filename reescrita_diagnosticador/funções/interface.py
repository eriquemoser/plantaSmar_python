def leiaInt(string):
    while True:
        try:
            s = int(input(string))
        except(ValueError, TypeError):
            print('\033[31m Tivemos um problema, digite novamente! \033[m')
            continue
        except (KeyboardInterrupt):
            print('\nO usuário preferiu não informar os dados')
            return 0
        else:
            return s
            break

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
