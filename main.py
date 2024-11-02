from src.compositions import *

domains = None
while (True):
    print("1 - Calcular a pertinência de um valor nas funções de um arquivo")
    print("2 - Calcular os graus de ativação de duas amostras para domínios aleatórios das funções de pertinência implemntada")
    print("3 - Gerar as operações nos domínios da opção anterior (Necessáio escolher a opção anterior antes desta)")
    print("4 - Gerar as relações entre os conjunto Meia-Idade e Alto nas T-normas Min Zadeh e Produto Algébrico e S-Normas Max Zadeh e Soma Probabilística")
    print("5 - Gerar as composições entres os conjuntos U={2, 12}, V={1, 7, 13} e W={4, 8}")
    print("0 - Para Sair")
    print("\nEscolha uma opção: ", end='')
    opcao = int(input())
    
    match opcao:
        case 1:
            print("\nQual o caminho do arquivo com as funções: ", end='')
            arquivo = input()
            AcharGrauPertinência(arquivo)
            print()
        case 2:
            print()
            domains = AcharGrauAtivacaoFuncoes()
            if domains != None:
                print("\nOs domínios estão na pasta data/imgs/domains\n")
            else:
                print("\nAs amostras precisam estar dentro do domíno\n")
        case 3:
            if (domains != None):
                MostrarOpercacoes(domains)
                print("\nAs operações estão na pasta data/imgs/operations\n")
            else:
                print()
        case 4:
            MostrarRelacao()
            print("\nAs relações estão na pasta data/imgs/relations\n")
        case 5:
            MostrarComposicao()
            print("\nAs composições estão na pasta data/imgs/compositions\n")
        case 0:
            break