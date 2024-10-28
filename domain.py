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
        for f in self.fncs:
            graus.append(f.calcularMi(x))
        return graus

    def plotarGrauAtivacao(self, x1, x2, directory):
        plt.figure(figsize=(10,8))
        x = np.linspace(self.inf, self.sup, 250)
        for f in self.fncs:
            y = []
            for i in x:
                y.append(f.calcularMi(i))
            plt.plot(x, y)
        plt.axvline(x1, color='cyan', linestyle='--', label=f'x={x1}')
        plt.axvline(x2, color='purple', linestyle='--', label=f'x={x2}')
        plt.title(self.fncs[0].name)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(directory + self.fncs[0].name + ".png")
        plt.close()

def gntTRfncs(inf, sup, centers, qtd):
    scale = 100
    max = 3
    funcs = []
    i = 0
    while i < qtd:
        f = Triangular(inf, sup)
        b = centers[i]
        i += 1
        a = rd.randrange(int((inf-max)*scale), int(b*scale), 1) / scale
        c = rd.randrange(int(b*scale), int((sup+max)*scale), 1) / scale
        if a == b:
            while c == b:
                c = rd.randrange(int(b*scale), int((sup+max)*scale), 1) / scale
        f.setValues(a, b, c)
        funcs.append(f)
    return funcs

def gntGSfncs(inf, sup, centers, qtd):
    scale = 100
    max = 5
    funcs = []
    i = 0
    while i < qtd:
        f = Gaussiana(inf, sup)
        c = centers[i]
        i += 1
        sigma = rd.randrange(0, int(max*scale), 1) / scale
        while sigma == 0:
            sigma = rd.randrange(0, int(max*scale), 1) / scale
        f.setValues(c, sigma)
        funcs.append(f)
    return funcs

def gntSGfncs(inf, sup, centers, qtd):
    scale = 100
    max = 5
    funcs = []
    i = 0
    while i < qtd:
        f = Sigmoidal(inf, sup)
        c = centers[i]
        i += 1
        a = rd.randrange(0, int(max*scale), 1) / scale
        f.setValues(a, c)
        funcs.append(f)
    return funcs

def gntCCfncs(inf, sup, centers, qtd):
    scale = 100
    max = 2
    min = 0.3
    funcs = []
    i = 0
    while i < qtd:
        f = Cauchy(inf, sup)
        x_0 = centers[i]
        i += 1
        gamma = rd.randrange(int(min*scale), int(max*scale), 1) / scale
        while gamma == 0:
            gamma = rd.randrange(int(min*scale), int(max*scale), 1) / scale
        f.setValues(x_0, gamma)
        funcs.append(f)
    return funcs

def gntGDfncs(inf, sup, centers, qtd):
    scale = 100
    max = 6
    funcs = []
    i = 0
    while i < qtd:
        f = GaussianaDupla(inf, sup)
        c = centers[i]
        i += 1
        sigma1 = rd.randrange(0, int(max*scale), 1) / scale
        while sigma1 == 0:
            sigma1 = rd.randrange(0, int(max*scale), 1) / scale
        sigma2 = rd.randrange(0, int(max*scale), 1) / scale
        while sigma2 == 0:
            sigma2 = rd.randrange(0, int(max*scale), 1) / scale
        f.setValues(c, sigma1, sigma2)
        funcs.append(f)
    return funcs

def gntLPfncs(inf, sup, centers, qtd):
    scale = 100
    max = 3
    min = 0.5
    funcs = []
    i = 0
    while i < qtd:
        f = Laplace(inf, sup)
        mi = centers[i]
        i += 1
        b = rd.randrange(int(min*scale), int(max*scale), 1) / scale
        f.setValues(mi, b)
        funcs.append(f)
    return funcs

def gntTPfncs(inf, sup, numbers, qtd):
    scale = 100
    max =  3
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            f = Trapezoidal(inf, sup)
            b = numbers[i]
            c = numbers[i+1]
            i += 1
            a = rd.randrange(int((inf-max)*scale), int(b*scale), 1) / scale
            d = rd.randrange(int(c*scale), int((sup+max)*scale), 1) / scale
            f.setValues(a, b, c, d)
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            f = Trapezoidal(inf, sup)
            b = numbers[i]
            c = numbers[i+1]
            i += 2
            a = rd.randrange(int((inf-max)*scale), int(b*scale), 1) / scale
            d = rd.randrange(int(c*scale), int((sup+max)*scale), 1) / scale
            f.setValues(a, b, c, d)
            funcs.append(f)
    return funcs

def gntSNfncs(inf, sup, numbers, qtd):
    scale = 100
    b = rd.randrange(int(1*scale), int(5*scale), 1) / scale
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            f = Sino(inf, sup)
            p1 = numbers[i]
            p2 = numbers[i+1]
            i += 1
            c = (p1 + p2) / 2
            a = abs(p2 - p1)
            f.setValues(a, b, c)
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            f = Sino(inf, sup)
            p1 = numbers[i]
            p2 = numbers[i+1]
            i += 2
            c = (p1 + p2) / 2
            a = abs(p2 - p1)
            f.setValues(a, b, c)
            funcs.append(f)    
    return funcs


def gntSSfncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            f = Sshaped(inf, sup)
            a = numbers[i]
            b = numbers[i+1]
            i += 1
            f.setValues(a, b)
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            f = Sshaped(inf, sup)
            a = numbers[i]
            b = numbers[i+1]
            i += 2
            f.setValues(a, b)
            funcs.append(f)
    return funcs

def gntZSfncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            f = Zshaped(inf, sup)
            a = numbers[i]
            b = numbers[i+1]
            i += 1
            f.setValues(a, b)
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            f = Zshaped(inf, sup)
            a = numbers[i]
            b = numbers[i+1]
            i += 2
            f.setValues(a, b)
            funcs.append(f)
    return funcs

def gntRTfncs(inf, sup, numbers, qtd):
    funcs = []
    i = 0
    if len(numbers) == qtd + 1:
        while i < qtd:
            f = Retangular(inf, sup)
            a = numbers[i]
            b = numbers[i+1]
            i += 1
            f.setValues(a, b)
            funcs.append(f)
    elif len(numbers) == qtd * 2:
        while i < qtd * 2:
            f = Retangular(inf, sup)
            a = numbers[i]
            b = numbers[i+1]
            i += 2
            f.setValues(a, b)
            funcs.append(f)
    return funcs

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
                    domain = Domain(inf, sup, funcs)
                case "GS":
                    funcs = gntGSfncs(inf, sup, centers, qtd)
                    domain = Domain(inf, sup, funcs)
                case "SG":
                    funcs = gntSGfncs(inf, sup, centers, qtd)
                    domain = Domain(inf, sup, funcs)
                case "CC":
                    funcs = gntCCfncs(inf, sup, centers, qtd)
                    domain = Domain(inf, sup, funcs)
                case "GD":
                    funcs = gntGDfncs(inf, sup, centers, qtd)
                    domain = Domain(inf, sup, funcs)
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
                    domain = Domain(inf, sup, funcs)
                case "SN":
                    funcs = gntSNfncs(inf, sup, numbers, qtd)
                    domain = Domain(inf, sup, funcs)
                case "SS":
                    funcs = gntSSfncs(inf, sup, numbers, qtd)
                    domain = Domain(inf, sup, funcs)
                case "ZS":
                    funcs = gntZSfncs(inf, sup, numbers, qtd)
                    domain = Domain(inf, sup, funcs)
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
        print(d.fncs[0].name)
        for g1, g2, i in zip(graus1, graus2, range(len(graus1))):
            print(f"\t- mi{i+1}(x1 = {x1}) = {g1} \t - mi{i+1}(x2 = {x2}) = {g2}")
        d.plotarGrauAtivacao(x1, x2, diterctory)
    return domains