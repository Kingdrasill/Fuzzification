from src.compositions import *

domains = None
while (True):
    print("1 - Calcular a pertinência de um valor nas funções de um arquivo")
    print("2 - Calcular os graus de ativação de duas amostras para domínios aleatórios das funções de pertinência implemntada")
    print("3 - Gerar as operações nos domínios da opção anterior (Necessáio escolher a opção anterior antes desta)")
    print("4 - Gerar 2 T-norma e 2 S-norma relações entre os conjunto Meia-Idade e Alto")
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
                print("\nOs domínios estão na pasta imgs/domains\n")
            else:
                print("\nAs amostras precisam estar dentro do domíno\n")
        case 3:
            if (domains != None):
                MostrarOpercacoes(domains)
                print("\nAs operações estão na pasta imgs/operations\n")
            else:
                print()
        case 4:
            ok = True
            ttipos, stipos = [], []
            tvalores, svalores = [], []
            tnomes, snomes = [], []
            print("\nTipos de T-Norma:\nM - Miz Zadeh\nP - Produto Algébrico\nL - Lukasiewicz\nH - Hamacher\nD - Diferença Limitada\nW - Weber Prod. Drástico")
            for n in range(2):
                print("Escolha uma opção: ", end='')
                tipo = input()
                match tipo:
                    case 'M':
                        tnomes.append("Miz Zadeh")
                        tvalores.append(None)
                    case 'P':
                        tnomes.append("Produto Algébrico")
                        tvalores.append(None)
                    case 'L':
                        tnomes.append("Lukasiewicz")
                        print("Qual o valor de p: ", end='')
                        valor = float(input())
                        tvalores.append(valor)
                    case 'H':
                        tnomes.append("Hamacher")
                        print("Qual o valor de gamma: ", end='')
                        valor = float(input())
                        tvalores.append(valor)
                    case 'D':
                        tnomes.append("Diferença Limitada")
                        tvalores.append(None)
                    case 'W':
                        tnomes.append("Weber Prod. Drástico")
                        tvalores.append(None)
                    case _:
                        print("\nTipo inválido\n")
                        ok = False
                        break
                ttipos.append(tipo)
            
            if ok:
                print("\nTipos de S-Norma:\nM - Max Zadeh\nP - Soma Probabilísitca\nL - Lukasiewicz\nH - Hamacher\nS - Soma Limitada\nW - Weber Soma Drástico")
                for n in range(2):
                    print("Escolha uma opção: ", end='')
                    tipo = input()
                    match tipo:
                        case 'M':
                            snomes.append("Miz Zadeh")
                            svalores.append(None)
                        case 'P':
                            snomes.append("Produto Algébrico")
                            svalores.append(None)
                        case 'L':
                            snomes.append("Lukasiewicz")
                            print("Qual o valor de p: ", end='')
                            valor = float(input())
                            svalores.append(valor)
                        case 'H':
                            snomes.append("Hamacher")
                            print("Qual o valor de gamma: ", end='')
                            valor = float(input())
                            svalores.append(valor)
                        case 'S':
                            snomes.append("Diferença Limitada")
                            svalores.append(None)
                        case 'W':
                            snomes.append("Weber Prod. Drástico")
                            svalores.append(None)
                        case _:
                            print("\nTipo inválido\n")
                            ok = False
                            break
                    stipos.append(tipo)

                if ok:
                    MostrarRelacao(ttipos, tvalores, tnomes, stipos, svalores, snomes)
                    print("\nAs relações estão na pasta imgs/relations\n")
        case 5:
            MostrarComposicao()
            print("\nAs composições estão na pasta imgs/compositions\n")
        case 0:
            break