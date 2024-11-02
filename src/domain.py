from src.functions import *
import random as rd
import matplotlib.pyplot as plt
import numpy as np

class Domain:
    def __init__(self, inferior, superior, funcs, name):
        self.inf = inferior
        self.sup = superior
        self.funcs = funcs
        self.name = name

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

def gntTRfuncs(inf, sup, centers, qtd):
    scale = 100
    max = 3
    funcs = []
    i = 0
    while i < qtd:
        b = centers[i]
        i += 1
        a = rd.randrange(int((inf-max)*scale), int(b*scale), 1) / scale
        c = rd.randrange(int(b*scale), int((sup+max)*scale), 1) / scale
        if a == b:
            while c == b:
                c = rd.randrange(int(b*scale), int((sup+max)*scale), 1) / scale
        f = {
            'tipo': 'TR',
            'values': [inf, sup, a, b, c],
            'func': CalcularMiTR
        }
        funcs.append(f)
    return ('Triangular', funcs)

def gntGSfuncs(inf, sup, centers, qtd):
    scale = 100
    max = 5
    min = 1
    funcs = []
    i = 0
    while i < qtd:
        c = centers[i]
        i += 1
        sigma = rd.randrange(min, int(max*scale), 1) / scale
        while sigma == 0:
            sigma = rd.randrange(min, int(max*scale), 1) / scale
        f = {
            'tipo': 'GS',
            'values': [inf, sup, c, sigma],
            'func': CalcularMiGS
        }
        funcs.append(f)
    return ('Gaussiana', funcs)

def gntSGfuncs(inf, sup, centers, qtd):
    scale = 100
    a = rd.randrange(0, int(5*scale), 1) / scale
    funcs = []
    i = 0
    while i < qtd:
        c = centers[i]
        i += 1
        f = {
            'tipo': 'SG',
            'values': [inf, sup, a, c],
            'func': CalcularMiSG
        }
        funcs.append(f)
    return ('Sigmoidal', funcs)

def gntCCfuncs(inf, sup, centers, qtd):
    scale = 100
    gamma = rd.randrange(int(0.3*scale), int(2*scale), 1) / scale
    while gamma == 0:
        gamma = rd.randrange(int(0.3*scale), int(2*scale), 1) / scale
    funcs = []
    i = 0
    while i < qtd:
        x_0 = centers[i]
        i += 1
        f = {
            'tipo': 'CC',
            'values': [inf, sup, x_0, gamma],
            'func': CalcularMiCC
        }
        funcs.append(f)
    return ('Cauchy', funcs)

def gntGDfuncs(inf, sup, centers, qtd):
    scale = 100
    sigma1 = rd.randrange(0, int(6*scale), 1) / scale
    while sigma1 == 0:
        sigma1 = rd.randrange(0, int(6*scale), 1) / scale
    sigma2 = rd.randrange(0, int(6*scale), 1) / scale
    while sigma2 == 0:
        sigma2 = rd.randrange(0, int(6*scale), 1) / scale
    funcs = []
    i = 0
    while i < qtd:
        c = centers[i]
        i += 1
        if (rd.choice([1,2]) == 1):
            f = {
                'tipo': 'GD',
                'values': [inf, sup, c, sigma1, sigma2],
                'func': CalcularMiGD
            }
        else:
            f = {
                'tipo': 'GD',
                'values': [inf, sup, c, sigma2, sigma1],
                'func': CalcularMiGD
            }
        funcs.append(f)
    return ('Gaussiana Dupla', funcs)

def gntLPfuncs(inf, sup, centers, qtd):
    scale = 100
    b = rd.randrange(int(0.5*scale), int(3*scale), 1) / scale
    funcs = []
    i = 0
    while i < qtd:
        mi = centers[i]
        i += 1
        f = {
            'tipo': 'LP',
            'values': [inf, sup, mi, b],
            'func': CalcularMiLP
        }
        funcs.append(f)
    return ('Laplace', funcs)

def gntTPfuncs(inf, sup, numbers, qtd):
    scale = 100
    max =  3
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            b = numbers[i]
            c = numbers[i+1]
            i += 1
            a = rd.randrange(int((inf-max)*scale), int(b*scale), 1) / scale
            d = rd.randrange(int(c*scale), int((sup+max)*scale), 1) / scale
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
            a = rd.randrange(int((inf-max)*scale), int(b*scale), 1) / scale
            d = rd.randrange(int(c*scale), int((sup+max)*scale), 1) / scale
            f = {
                'tipo': 'TP',
                'values': [inf, sup, a, b, c, d],
                'func': CalcularMiTP
            }
            funcs.append(f)
    return ('Trapezoidal', funcs)

def gntSNfuncs(inf, sup, numbers, qtd):
    scale = 100
    b = rd.randrange(int(1*scale), int(5*scale), 1) / scale
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            p1 = numbers[i]
            p2 = numbers[i+1]
            i += 1
            c = (p1 + p2) / 2
            a = abs(p2 - p1)
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
            f = {
                'tipo': 'SN',
                'values': [inf, sup, a, b, c],
                'func': CalcularMiSN
            }
            funcs.append(f)
    return ('Sino', funcs)

def gntSSfuncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            a = numbers[i]
            b = numbers[i+1]
            i += 1
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
            f = {
                'tipo': 'SS',
                'values': [inf, sup, a, b],
                'func': CalcularMiSS
            }
            funcs.append(f)
    return ('S-shaped', funcs)

def gntZSfuncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            a = numbers[i]
            b = numbers[i+1]
            i += 1
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
            f = {
                'tipo': 'ZS',
                'values': [inf, sup, a, b],
                'func': CalcularMiZS
            }
            funcs.append(f)
    return ('Z-shaped', funcs)

def gntRTfuncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            a = numbers[i]
            b = numbers[i+1]
            i += 1
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
            f = {
                'tipo': 'RT',
                'values': [inf, sup, a, b],
                'func': CalcularMiRT
            }
            funcs.append(f)
    return ('Retangular', funcs)

def gntDomain(inf, sup, function, qtd):
    domain = None

    match function:
        case w if w in ["TR", "GS", "SG", "CC", "GD", "LP"]:
            points = rd.choice(['S', 'M', 'E', '0'])
            match points:
                case 'S':
                    centers = np.linspace(inf, sup, num=qtd + 1)[1:]
                case 'M':
                    centers = np.linspace(inf, sup, num=qtd + 2)[1:-1]
                case 'E':
                    centers = np.linspace(inf, sup, num=qtd + 1)[:-1]
                case '0':
                    centers = np.linspace(inf, sup, num=qtd)
            
            match w:
                case "TR":
                    name, funcs = gntTRfuncs(inf, sup, centers, qtd)
                case "GS":
                    name, funcs = gntGSfuncs(inf, sup, centers, qtd)
                case "SG":
                    name, funcs = gntSGfuncs(inf, sup, centers, qtd)
                case "CC":
                    name, funcs = gntCCfuncs(inf, sup, centers, qtd)
                case "GD":
                    name, funcs = gntGDfuncs(inf, sup, centers, qtd)
                case "LP":
                    name, funcs = gntLPfuncs(inf, sup, centers, qtd)

            domain = Domain(inf, sup, funcs, name)

        case w if w in ["TP", "SN", "SS", "ZS", "RT"]:
            points = rd.choice(['C', "M"])
            match points:
                case 'C':
                    tipo1 = rd.choice(["F", "H"])
                    match tipo1:
                        case "F":
                            numbers = np.linspace(inf, sup, num=qtd + 1)
                        case "H":
                            tipo2 = rd.choice([1, 2, 3])
                            match tipo2:
                                case 1:
                                    numbers = np.linspace(inf, sup, num=(qtd * 2) + 1)[:-1]
                                case 2:
                                    numbers = np.linspace(inf, sup, num=(qtd * 2))
                                case 3:
                                    numbers = np.linspace(inf, sup, num=(qtd * 2) + 1)[1:]
                case 'M':
                    numbers = np.linspace(inf, sup, num=(qtd * 2) + 2)[1:-1]

            match w:
                case "TP":
                    name, funcs = gntTPfuncs(inf, sup, numbers, qtd)
                case "SN":
                    name, funcs = gntSNfuncs(inf, sup, numbers, qtd)
                case "SS":
                    name, funcs = gntSSfuncs(inf, sup, numbers, qtd)
                case "ZS":
                    name, funcs = gntZSfuncs(inf, sup, numbers, qtd)
                case "RT":
                    name, funcs = gntRTfuncs(inf, sup, numbers, qtd)

            domain = Domain(inf, sup, funcs, name)

    return domain

def AcharGrauAtivacaoFuncoes(diterctory="imgs/domains/"):
    inf = 0
    sup = 10
    qtd = rd.choice([4, 5, 6])

    print(f"Valor de x1 no domínio [{inf}, {sup}]: ", end='')
    x1 = float(input())

    print(f"Valor de x2 no domíno [{inf}, {sup}]: ", end='')
    x2 = float(input())

    if (x1 >= inf and x1 <= sup and x2 >=inf and x2 <= sup):
        f = open(diterctory + "resultados.txt", "w")
        domains = []
        for z in ["TR", "TP", "GS", "SG", "SN", "SS", "ZS", "CC", "GD", "RT", "LP"]:
            d = gntDomain(inf, sup, z, qtd)
            domains.append(d)
            graus1 = d.calcularGrauAtivacao(x1)
            graus2 = d.calcularGrauAtivacao(x2)
            f.write(d.name + '\n')
            for g1, g2, i in zip(graus1, graus2, range(len(graus1))):
                f.write(f'f{i+1} - x={x1} = {g1:.4f} \t\t x={x2} = {g2:.4f}\n')
            f.write('\n')
            d.plotarGrauAtivacao(x1, x2, diterctory)
        f.close()
    else:
        return None
    return domains