from src.functions import *
import random as rd
import matplotlib.pyplot as plt
import numpy as np

# Classe usada para guardar informações de um domínio
class Domain:
    # A classe possui limites inf e sup, um nome e as informações das funções
    def __init__(self, inferior, superior, funcs, name):
        self.inf = inferior
        self.sup = superior
        self.funcs = funcs
        self.name = name

    # Calcula e retorna os graus de ativação de uma amostra, a chamada da função depende de seu tipo
    def calcularGrauAtivacao(self, x):
        graus = []
        for f in self.funcs:
            match f['tipo']:
                case w if w in ['GS', 'SG', 'SS', 'ZS', 'CC', 'RT', 'LP']:
                    graus.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], x))
                case w if w in ['TR', 'SN', 'GD']:
                    graus.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], f['values'][4], x))
                case w if w in ['TP']:
                    graus.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], f['values'][4], f['values'][5], x))
        return graus

    # Plota e salva o gráfio do domínio, suas funções e onde estão as amostras no domínio
    def plotarGrauAtivacao(self, x1, x2, directory):
        plt.figure(figsize=(10,8))
        x = np.linspace(self.inf, self.sup, 500)
        for f in self.funcs:
            y = []
            match f['tipo']:
                case w if w in ['GS', 'SG', 'SS', 'ZS', 'CC', 'RT', 'LP']:
                    for i in x:
                        y.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], i))
                case w if w in ['TR', 'SN', 'GD']:
                    for i in x:
                        y.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], f['values'][4], i))
                case w if w in ['TP']:
                    for i in x:
                        y.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], f['values'][4], f['values'][5], i))
            plt.plot(x, y)
        plt.axvline(x1, linestyle='--', color='purple', label=f'x={x1}')
        plt.axvline(x2, linestyle='--', color='black', label=f'x={x2}')
        plt.title(self.name)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(directory + self.name + ".png")
        plt.close()

# Gera funções triangualar uniformente separadas
def gntTRfuncs(inf, sup, centers, qtd):
    scale = 100
    max = 3
    # Armazena todos as funções
    funcs = []
    i = 0
    while i < qtd:
        b = centers[i]
        i += 1
        # Gera aletoriamente os valores que não são o centro
        a = rd.randrange(int((inf-max)*scale), int(b*scale), 1) / scale
        c = rd.randrange(int(b*scale), int((sup+max)*scale), 1) / scale
        if a == b:
            while c == b:
                c = rd.randrange(int(b*scale), int((sup+max)*scale), 1) / scale
        # Cada função tem seu tipo, valores e qual a função a ser chamada
        f = {
            'tipo': 'TR',
            'values': [inf, sup, a, b, c],
            'func': CalcularMiTR
        }
        funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Triangular', funcs)

# Gera funções gaussiana uniformente separadas
def gntGSfuncs(inf, sup, centers, qtd):
    scale = 100
    max = 5
    min = 1
    # Armazena todos as funções
    funcs = []
    i = 0
    while i < qtd:
        c = centers[i]
        i += 1
        # Gera aletoriamente o valor que não é o centro
        sigma = rd.randrange(min, int(max*scale), 1) / scale
        while sigma == 0:
            sigma = rd.randrange(min, int(max*scale), 1) / scale
        # Cada função tem seu tipo, valores e qual a função a ser chamada
        f = {
            'tipo': 'GS',
            'values': [inf, sup, c, sigma],
            'func': CalcularMiGS
        }
        funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Gaussiana', funcs)

# Gera funções sigmoidal uniformente separadas
def gntSGfuncs(inf, sup, centers, qtd):
    scale = 100
    # Gera aletoriamente o valor que não é o centro que é igual para todas as funções
    a = rd.randrange(0, int(5*scale), 1) / scale
    # Armazena todos as funções
    funcs = []
    i = 0
    while i < qtd:
        c = centers[i]
        i += 1
        # Cada função tem seu tipo, valores e qual a função a ser chamada
        f = {
            'tipo': 'SG',
            'values': [inf, sup, a, c],
            'func': CalcularMiSG
        }
        funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Sigmoidal', funcs)

# Gera funções cauchy uniformente separadas
def gntCCfuncs(inf, sup, centers, qtd):
    scale = 100
    # Gera aletoriamente o valor que não é o centro que é igual para todas as funções
    gamma = rd.randrange(int(0.3*scale), int(2*scale), 1) / scale
    while gamma == 0:
        gamma = rd.randrange(int(0.3*scale), int(2*scale), 1) / scale
    # Armazena todos as funções
    funcs = []
    i = 0
    while i < qtd:
        x_0 = centers[i]
        i += 1
        # Cada função tem seu tipo, valores e qual a função a ser chamada
        f = {
            'tipo': 'CC',
            'values': [inf, sup, x_0, gamma],
            'func': CalcularMiCC
        }
        funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Cauchy', funcs)

# Gera funções gaussiana dupla uniformente separadas
def gntGDfuncs(inf, sup, centers, qtd):
    scale = 100
    # Gera aletoriamente os valores que não são o centro que são iguais para todas as funções
    sigma1 = rd.randrange(0, int(6*scale), 1) / scale
    while sigma1 == 0:
        sigma1 = rd.randrange(0, int(6*scale), 1) / scale
    sigma2 = rd.randrange(0, int(6*scale), 1) / scale
    while sigma2 == 0:
        sigma2 = rd.randrange(0, int(6*scale), 1) / scale
    # Armazena todos as funções
    funcs = []
    i = 0
    while i < qtd:
        c = centers[i]
        i += 1
        # Decide se intervi o sigma1 com o sigma2
        if (rd.choice([1,2]) == 1):
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'GD',
                'values': [inf, sup, c, sigma1, sigma2],
                'func': CalcularMiGD
            }
        else:
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'GD',
                'values': [inf, sup, c, sigma2, sigma1],
                'func': CalcularMiGD
            }
        funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Gaussiana Dupla', funcs)

# Gera funções laplace uniformente separadas
def gntLPfuncs(inf, sup, centers, qtd):
    scale = 100
    # Gera aletoriamente o valor que não é o centro que é igual para todas as funções
    b = rd.randrange(int(0.5*scale), int(3*scale), 1) / scale
    # Armazena todos as funções
    funcs = []
    i = 0
    while i < qtd:
        mi = centers[i]
        i += 1
        # Cada função tem seu tipo, valores e qual a função a ser chamada
        f = {
            'tipo': 'LP',
            'values': [inf, sup, mi, b],
            'func': CalcularMiLP
        }
        funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Laplace', funcs)

# Gera funções trapezoidal uniformente separadas
def gntTPfuncs(inf, sup, numbers, qtd):
    scale = 100
    max =  3
    # Armazena todos as funções
    funcs = []
    i = 0
    # A quantidade de valores que definem os intervalos é diferente
    if len(numbers) == qtd + 1:
        while i < qtd:
            b = numbers[i]
            c = numbers[i+1]
            i += 1
            # Gera aletoriamente os valores que não são do intervalo central
            a = rd.randrange(int((inf-max)*scale), int(b*scale), 1) / scale
            d = rd.randrange(int(c*scale), int((sup+max)*scale), 1) / scale
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'TP',
                'values': [inf, sup, a, b, c, d],
                'func': CalcularMiTP
            }
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            b = numbers[i]
            c = numbers[i+1]
            i += 2
            # Gera aletoriamente os valores que não são do intervalo central
            a = rd.randrange(int((inf-max)*scale), int(b*scale), 1) / scale
            d = rd.randrange(int(c*scale), int((sup+max)*scale), 1) / scale
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'TP',
                'values': [inf, sup, a, b, c, d],
                'func': CalcularMiTP
            }
            funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Trapezoidal', funcs)

# Gera funções sino uniformente separadas
def gntSNfuncs(inf, sup, numbers, qtd):
    scale = 100
    # Gera aletoriamente o valor que não é do intervalo central que é igual para todas as funções
    b = rd.randrange(int(1*scale), int(5*scale), 1) / scale
    funcs = []
    i = 0
    # A quantidade de valores que definem os intervalos é diferente
    if len(numbers) == qtd + 1:
        while i < qtd:
            p1 = numbers[i]
            p2 = numbers[i+1]
            i += 1
            c = (p1 + p2) / 2
            a = abs(p2 - p1)
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'SN',
                'values': [inf, sup, a, b, c],
                'func': CalcularMiSN
            }
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            p1 = numbers[i]
            p2 = numbers[i+1]
            i += 2
            c = (p1 + p2) / 2
            a = abs(p2 - p1)
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'SN',
                'values': [inf, sup, a, b, c],
                'func': CalcularMiSN
            }
            funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Sino', funcs)

# Gera funções S uniformente separadas
def gntSSfuncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    # A quantidade de valores que definem os intervalos é diferente
    if len(numbers) == qtd + 1:
        while i < qtd:
            a = numbers[i]
            b = numbers[i+1]
            i += 1
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'SS',
                'values': [inf, sup, a, b],
                'func': CalcularMiSS
            }
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            a = numbers[i]
            b = numbers[i+1]
            i += 2
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'SS',
                'values': [inf, sup, a, b],
                'func': CalcularMiSS
            }
            funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('S-shaped', funcs)

# Gera funções Z uniformente separadas
def gntZSfuncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    # A quantidade de valores que definem os intervalos é diferente
    if len(numbers) == qtd + 1:
        while i < qtd:
            a = numbers[i]
            b = numbers[i+1]
            i += 1
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'ZS',
                'values': [inf, sup, a, b],
                'func': CalcularMiZS
            }
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            a = numbers[i]
            b = numbers[i+1]
            i += 2
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'ZS',
                'values': [inf, sup, a, b],
                'func': CalcularMiZS
            }
            funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Z-shaped', funcs)

# Gera funções retangular uniformente separadas
def gntRTfuncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    # A quantidade de valores que definem os intervalos é diferente
    if len(numbers) == qtd + 1:
        while i < qtd:
            a = numbers[i]
            b = numbers[i+1]
            i += 1
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'RT',
                'values': [inf, sup, a, b],
                'func': CalcularMiRT
            }
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            a = numbers[i]
            b = numbers[i+1]
            i += 2
            # Cada função tem seu tipo, valores e qual a função a ser chamada
            f = {
                'tipo': 'RT',
                'values': [inf, sup, a, b],
                'func': CalcularMiRT
            }
            funcs.append(f)
    # Retorna o nome do domínio e as funções geradas
    return ('Retangular', funcs)

# Gera um domínio com qtd (quantidade) de funções do tipo function 
def gntDomain(inf, sup, function, qtd):
    domain = None

    # Verifica qual o tipo da função
    match function:
        # Funções de centro máximo
        case w if w in ["TR", "GS", "SG", "CC", "GD", "LP"]:
            # Decide como as funções vão ser igualmente espaçadas
            points = rd.choice(['S', 'M', 'E', '0'])
            match points:
                # A primeira função é centrada no início do limite do domínio
                case 'S':
                    centers = np.linspace(inf, sup, num=qtd + 1)[1:]
                # As funções não tem centros nos limites
                case 'M':
                    centers = np.linspace(inf, sup, num=qtd + 2)[1:-1]
                # A última função é centrada no fim do limite do domínio
                case 'E':
                    centers = np.linspace(inf, sup, num=qtd + 1)[:-1]
                # A primeira e a última função são centradas nos limites do domínio
                case '0':
                    centers = np.linspace(inf, sup, num=qtd)
            
            # Verifica qual o tipo de função com centro máximo
            match w:
                # Gera funções triangulares
                case "TR":
                    name, funcs = gntTRfuncs(inf, sup, centers, qtd)
                # Gera funções gaussianas
                case "GS":
                    name, funcs = gntGSfuncs(inf, sup, centers, qtd)
                # Gera funções sigmoidais
                case "SG":
                    name, funcs = gntSGfuncs(inf, sup, centers, qtd)
                # Gera funções cauchys
                case "CC":
                    name, funcs = gntCCfuncs(inf, sup, centers, qtd)
                # Gera funções gaussianas duplas
                case "GD":
                    name, funcs = gntGDfuncs(inf, sup, centers, qtd)
                # Gera funções laplaces
                case "LP":
                    name, funcs = gntLPfuncs(inf, sup, centers, qtd)

            domain = Domain(inf, sup, funcs, name)
        
        # Funções de intervalo máximo
        case w if w in ["TP", "SN", "SS", "ZS", "RT"]:
            # Decide como as funções vão ser igualmente espaçadas
            points = rd.choice(['C', "M"])
            match points:
                # Algum intervalo encosta no limite
                case 'C':
                    # Decide se os intervalos vão cobrir todo o domínio ou see vai ter um buraco entre cada intervalo
                    tipo1 = rd.choice(["F", "H"])
                    match tipo1:
                        # Totalmente cheio o domínio
                        case "F":
                            numbers = np.linspace(inf, sup, num=qtd + 1)
                        # Buracos entre os intervalos
                        case "H":
                            tipo2 = rd.choice([1, 2, 3])
                            match tipo2:
                                # A primeira função possui o intervalo máximo que começa no limite
                                case 1:
                                    numbers = np.linspace(inf, sup, num=(qtd * 2) + 1)[:-1]
                                # A primeira e a última funções possuem os intervalos máximo que começam no limite
                                case 2:
                                    numbers = np.linspace(inf, sup, num=(qtd * 2))
                                # A última função possui o intervalo máximo que começa no limite
                                case 3:
                                    numbers = np.linspace(inf, sup, num=(qtd * 2) + 1)[1:]
                # Todos os intervalos máximos não encostam nos limites
                case 'M':
                    numbers = np.linspace(inf, sup, num=(qtd * 2) + 2)[1:-1]
            
            # Verifica qual o tipo de função com intervalo máximo
            match w:
                # Gera funções trapezoidais
                case "TP":
                    name, funcs = gntTPfuncs(inf, sup, numbers, qtd)
                # Gera funções sinos
                case "SN":
                    name, funcs = gntSNfuncs(inf, sup, numbers, qtd)
                # Gera funções Ss
                case "SS":
                    name, funcs = gntSSfuncs(inf, sup, numbers, qtd)
                # Gera funções Zs
                case "ZS":
                    name, funcs = gntZSfuncs(inf, sup, numbers, qtd)
                # Gera funções retangulares
                case "RT":
                    name, funcs = gntRTfuncs(inf, sup, numbers, qtd)

            # Instância o domínio
            domain = Domain(inf, sup, funcs, name)

    return domain

# Função para achar os graus de ativação de duas amostras em domínios diferentes e
# plotar os domínios, o arquivo resultados.txt aramazena os graus de ativação e cada
# domínio gera um gráfico do domínio.
# Retorna os domínios criados para uso em outro lugar
def AcharGrauAtivacaoFuncoes(diterctory="imgs/domains/"):
    # Limites do domínio
    inf, sup = 0, 10
    # Quantidade de funções no domínio
    qtd = rd.choice([4, 5, 6])

    # Pega o valor da primeira amostra
    print(f"Valor de x1 no domínio [{inf}, {sup}]: ", end='')
    x1 = float(input())

    # pega o valor da segunda amostra
    print(f"Valor de x2 no domíno [{inf}, {sup}]: ", end='')
    x2 = float(input())

    # Verifica se as amostras estão dentro dos limites
    if (x1 >= inf and x1 <= sup and x2 >=inf and x2 <= sup):
        f = open(diterctory + "resultados.txt", "w")

        # Armazena os domínios criados
        domains = []

        # Para cada função de pertinência cria um domínio com funções do seu tipo
        for z in ["TR", "TP", "GS", "SG", "SN", "SS", "ZS", "CC", "GD", "RT", "LP"]:
            # Gera um domínio aleatório com funções de um tipo específico
            d = gntDomain(inf, sup, z, qtd)
            domains.append(d)

            # Calcula os graus de ativação da amostra 1 e da amostra 2
            graus1 = d.calcularGrauAtivacao(x1)
            graus2 = d.calcularGrauAtivacao(x2)

            # Escreve os valores dos graus no arquivo resultados.txt
            f.write(d.name + '\n')
            for g1, g2, i in zip(graus1, graus2, range(len(graus1))):
                f.write(f'f{i+1} - x={x1} = {g1:.4f} \t\t x={x2} = {g2:.4f}\n')
            f.write('\n')

            # Plota o gráfico do domínio e salva ele num arquivo
            d.plotarGrauAtivacao(x1, x2, diterctory)
        f.close()
    else:
        return None
    return domains