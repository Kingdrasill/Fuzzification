from functions import *
import random as rd
import matplotlib.pyplot as plt
import numpy as np

class Domain:
    def __init__(self, inferior, superior, funcs):
        self.inf = inferior
        self.sup = superior
        self.fncs = funcs

    def calcularGrauAtivacao(self, x):
        graus = []
        match self.fncs['tipo']:
            case w if w in ['GS', 'SG', 'SS', 'ZS', 'CC', 'RT', 'LP']:
                for f in self.fncs['funcs']:
                    graus.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], x))
            case w if w in ['TR', 'SN', 'GD']:
                for f in self.fncs['funcs']:
                    graus.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], f['values'][4], x))
            case w if w in ['TP']:
                for f in self.fncs['funcs']:
                    graus.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], f['values'][4], f['values'][5], x))
        return graus

    def plotarGrauAtivacao(self, x1, x2, directory):
        plt.figure(figsize=(10,8))
        x = np.linspace(self.inf, self.sup, 250)
        ys = []
        match self.fncs['tipo']:
            case w if w in ['GS', 'SG', 'SS', 'ZS', 'CC', 'RT', 'LP']:
                for f in self.fncs['funcs']:
                    y = []
                    for i in x:
                        y.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], i))
                    ys.append(y)
            case w if w in ['TR', 'SN', 'GD']:
                for f in self.fncs['funcs']:
                    y = []
                    for i in x:
                        y.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], f['values'][4], i))
                    ys.append(y)
            case w if w in ['TP']:
                for f in self.fncs['funcs']:
                    y = []
                    for i in x:
                        y.append(f['func'](f['values'][0], f['values'][1], f['values'][2], f['values'][3], f['values'][4], f['values'][5], i))
                    ys.append(y)
        for y in ys:
            plt.plot(x, y)
        plt.axvline(x1, color='cyan', linestyle='--', label=f'x={x1}')
        plt.axvline(x2, color='purple', linestyle='--', label=f'x={x2}')
        plt.title(self.fncs['name'])
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(directory + self.fncs['name'] + ".png")
        plt.close()

def gntTRfncs(inf, sup, centers, qtd):
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
            'values': [inf, sup, a, b, c],
            'func': CalcularMiTR
        }
        funcs.append(f)
    return {'tipo': 'TR', 'name': 'Triangular', 'funcs': funcs}

def gntGSfncs(inf, sup, centers, qtd):
    scale = 100
    max = 5
    funcs = []
    i = 0
    while i < qtd:
        c = centers[i]
        i += 1
        sigma = rd.randrange(0, int(max*scale), 1) / scale
        while sigma == 0:
            sigma = rd.randrange(0, int(max*scale), 1) / scale
        f = {
            'values': [inf, sup, c, sigma],
            'func': CalcularMiGS
        }
        funcs.append(f)
    return {'tipo': 'GS', 'name': 'Gaussiana', 'funcs': funcs}

def gntSGfncs(inf, sup, centers, qtd):
    scale = 100
    max = 5
    funcs = []
    i = 0
    while i < qtd:
        c = centers[i]
        i += 1
        a = rd.randrange(0, int(max*scale), 1) / scale
        f = {
            'values': [inf, sup, a, c],
            'func': CalcularMiSG
        }
        funcs.append(f)
    return {'tipo': 'SG', 'name': 'Sigmoidal', 'funcs': funcs}

def gntCCfncs(inf, sup, centers, qtd):
    scale = 100
    max = 2
    min = 0.3
    funcs = []
    i = 0
    while i < qtd:
        x_0 = centers[i]
        i += 1
        gamma = rd.randrange(int(min*scale), int(max*scale), 1) / scale
        while gamma == 0:
            gamma = rd.randrange(int(min*scale), int(max*scale), 1) / scale
        f = {
            'values': [inf, sup, x_0, gamma],
            'func': CalcularMiCC
        }
        funcs.append(f)
    return {'tipo': 'CC', 'name': 'Cauchy', 'funcs': funcs}

def gntGDfncs(inf, sup, centers, qtd):
    scale = 100
    max = 6
    funcs = []
    i = 0
    while i < qtd:
        c = centers[i]
        i += 1
        sigma1 = rd.randrange(0, int(max*scale), 1) / scale
        while sigma1 == 0:
            sigma1 = rd.randrange(0, int(max*scale), 1) / scale
        sigma2 = rd.randrange(0, int(max*scale), 1) / scale
        while sigma2 == 0:
            sigma2 = rd.randrange(0, int(max*scale), 1) / scale
        f = {
            'values': [inf, sup, c, sigma1, sigma2],
            'func': CalcularMiGD
        }
        funcs.append(f)
    return {'tipo': 'GD', 'name': 'Gaussiana Dupla', 'funcs': funcs}

def gntLPfncs(inf, sup, centers, qtd):
    scale = 100
    max = 3
    min = 0.5
    funcs = []
    i = 0
    while i < qtd:
        mi = centers[i]
        i += 1
        b = rd.randrange(int(min*scale), int(max*scale), 1) / scale
        f = {
            'values': [inf, sup, mi, b],
            'func': CalcularMiLP
        }
        funcs.append(f)
    return {'tipo': 'LP', 'name': 'Laplace', 'funcs': funcs}

def gntTPfncs(inf, sup, numbers, qtd):
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
                'values': [inf, sup, a, b, c, d],
                'func': CalcularMiTP
            }
            funcs.append(f)
    return {'tipo': 'TP', 'name': 'Trapezoidal', 'funcs': funcs}

def gntSNfncs(inf, sup, numbers, qtd):
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
                'values': [inf, sup, a, b, c],
                'func': CalcularMiSN
            }
            funcs.append(f)
    return {'tipo': 'SN', 'name': 'Sino', 'funcs': funcs}

def gntSSfncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            a = numbers[i]
            b = numbers[i+1]
            i += 1
            f = {
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
                'values': [inf, sup, a, b],
                'func': CalcularMiSS
            }
            funcs.append(f)
    return {'tipo': 'SS', 'name': 'S-shaped', 'funcs': funcs}

def gntZSfncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            a = numbers[i]
            b = numbers[i+1]
            i += 1
            f = {
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
                'values': [inf, sup, a, b],
                'func': CalcularMiZS
            }
            funcs.append(f)
    return {'tipo': 'ZS', 'name': 'Z-shaped', 'funcs': funcs}

def gntRTfncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            a = numbers[i]
            b = numbers[i+1]
            i += 1
            f = {
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
                'values': [inf, sup, a, b],
                'func': CalcularMiRT
            }
            funcs.append(f)
    return {'tipo': 'RT', 'name': 'Retangular', 'funcs': funcs}

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
                    funcs = gntTRfncs(inf, sup, centers, qtd)
                case "GS":
                    funcs = gntGSfncs(inf, sup, centers, qtd)
                case "SG":
                    funcs = gntSGfncs(inf, sup, centers, qtd)
                case "CC":
                    funcs = gntCCfncs(inf, sup, centers, qtd)
                case "GD":
                    funcs = gntGDfncs(inf, sup, centers, qtd)
                case "LP":
                    funcs = gntLPfncs(inf, sup, centers, qtd)
            domain = Domain(inf, sup, funcs)

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
                    funcs = gntTPfncs(inf, sup, numbers, qtd)
                case "SN":
                    funcs = gntSNfncs(inf, sup, numbers, qtd)
                case "SS":
                    funcs = gntSSfncs(inf, sup, numbers, qtd)
                case "ZS":
                    funcs = gntZSfncs(inf, sup, numbers, qtd)
                case "RT":
                    funcs = gntRTfncs(inf, sup, numbers, qtd)
            domain = Domain(inf, sup, funcs)

    return domain

def AcharGrauAtivacaoFuncoes(diterctory="data/imgs/domains/"):
    inf = 0
    sup = 10
    qtd = rd.choice([4, 5, 6])

    print("Valor de x1: ", end='')
    x1 = float(input())

    print("Valor de x2: ", end='')
    x2 = float(input())

    domains = []
    for z in ["TR", "TP", "GS", "SG", "SN", "SS", "ZS", "CC", "GD", "RT", "LP"]:
        d = gntDomain(inf, sup, z, qtd)
        domains.append(d)
        graus1 = d.calcularGrauAtivacao(x1)
        graus2 = d.calcularGrauAtivacao(x2)
        print(d.fncs['name'])
        for g1, g2, i in zip(graus1, graus2, range(len(graus1))):
            print(f"\t- mi{i+1}(x1 = {x1}) = {g1} \t - mi{i+1}(x2 = {x2}) = {g2}")
        d.plotarGrauAtivacao(x1, x2, diterctory)
    return domains

domains = AcharGrauAtivacaoFuncoes()