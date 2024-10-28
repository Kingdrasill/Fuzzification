import math

def CalcularMiTR(inf, sup, a, b, c, x):
    if a > b or c < b:
        return "Algum valor de forma está errado"
    
    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    if (x <= a):
        return 0
    elif (x > a and x <= b):
        return ((x - a) / (b - a))
    elif (x > b and x <= c):
        return ((c - x) / (c - b))
    elif (x > c):
        return 0
    
def CalcularMiTP(inf, sup, a, b, c, d, x):
    if a > b or b > c or c > d:
        return "Algum valor de forma está errado"
    
    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    if (x <= a):
        return 0
    elif (x > a and x <= b):
        return ((x - a) / (b - a))
    elif (x > b and x <= c):
        return 1
    elif (x > c and x <= d):
        return ((d - x) / (d - c))
    elif (x > d):
        return 0
    
def CalcularMiGS(inf, sup, c, sigma, x):
    if (sigma == 0):
        return "Algum valor de forma está errado"

    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    return math.exp(-((x - c) ** 2)/(2 * sigma ** 2))

def CalcularMiSG(inf, sup, a, c, x):
    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    return (1 / (1 + math.exp(((-a) * (x - c)))))

def CalcularMiSN(inf, sup, a, b, c, x):
    if (a == 0):
        return "Algum valor de forma está errado"

    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    return (1 / (1 + (abs((x - c) / a)**(2 * b))))

def CalcularMiSS(inf, sup, a, b, x):
    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    if (x <= a):
        return 0
    elif (x > a and x <= ((a + b) / 2)):
        return (2 * (((x - a) / (b - a)) ** 2))
    elif (x > ((a + b) / 2) and x <= b):
        return (1 - 2 * (((b - x) / (b - a)) ** 2))
    elif (x > b):
        return 1
    
def CalcularMiZS(inf, sup, a, b , x):
    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    if (x <= a):
        return 1
    elif (x > a and x <= ((a + b) / 2)):
        return (1 - 2 * (((x - a) / (b - a)) ** 2))
    elif (x > ((a + b) / 2) and x <= b):
        return (2 * (((b - x) / (b - a)) ** 2))
    elif (x > b):
        return 0

def CalcularMiCC(inf, sup, x_0, gamma, x):
    if (gamma == 0):
        return "Algum valor de forma está errado"

    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    return (1 / ((math.pi * gamma) * (1 + ((x - x_0) / gamma) ** 2)))

def CalcularMiGD(inf, sup, mi, sigma1, sigma2, x):
    if (sigma1 == 0 or sigma2 == 0):
        return "Algum valor de forma está errado"

    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    A = math.sqrt(2 / math.pi) * (sigma1 + sigma2) ** (-1)

    if (x < mi):
        return (A * math.exp(-((x - mi) ** 2 / (2 * (sigma1 ** 2)))))
    else:
        return (A * math.exp(-((x - mi) ** 2 / (2 * (sigma2 ** 2)))))

def CalcularMiRT(inf, sup, a, b, x):
    if (a > b):
        return "Algum valor de forma está errado"
    
    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    if (x >= a and x <= b):
        return 1
    else:
        return 0
    
def CalcularMiLP(inf, sup, mi, b, x):
    if (b == 0):
        return "Algum valor de forma está errado"
    
    if (x < inf or x > sup):
        return "Valor x fora dos limites da função"
    
    return ((1 / (2 * b)) * math.exp(- (abs(x - mi)) / b))

def AcharGrauPertinência():
    f = open("data/functions.txt", "r")

    inf = 0
    sup = 10

    print("Valor de x: ", end='')
    x = float(input())

    for l in f:
        line = (l.strip()).split()
        match line[0]:
            case 'TR':
                if (len(line) == 4):
                    value = CalcularMiTR(inf, sup, float(line[1]), float(line[2]), float(line[3]), x)
                    print("Triangular: ", value)
                else:
                    print("Triangular: Está faltando valor da forma")
            case 'TP':
                if (len(line) == 5):
                    value = CalcularMiTP(inf, sup, float(line[1]), float(line[2]), float(line[3]), float(line[4]), x)
                    print("Trapezoidal: ", value)
                else:
                    print("Trapezoidal: Está faltando valor da forma")
            case 'GS':
                if (len(line) == 3):
                    value = CalcularMiGS(inf, sup, float(line[1]), float(line[2]), x)
                    print("Gaussiana: ", value)
                else:
                    print("Gaussiana: Está faltando valor da forma")
            case 'SG':
                if (len(line) == 3):
                    value = CalcularMiSG(inf, sup, float(line[1]), float(line[2]), x)
                    print("Sigmoidal: ", value)
                else:
                    print("Sigmoidal: Está faltando valor da forma")
            case 'SN':
                if (len(line) == 4):
                    value = CalcularMiSN(inf, sup, float(line[1]), float(line[2]), float(line[3]), x)
                    print("Sino: ", value)
                else:
                    print("Sino: Está faltando valor da forma")
            case 'SS':
                if (len(line) == 3):
                    value = CalcularMiSS(inf, sup, float(line[1]), float(line[2]), x)
                    print("S-shaped: ", value)
                else:
                    print("S-shaped: Está faltando valor da forma")
            case 'ZS':
                if (len(line) == 3):
                    value = CalcularMiZS(inf, sup, float(line[1]), float(line[2]), x)
                    print("Z-shaped: ", value)
                else:
                    print("Z-shaped: Está faltando valor da forma")
            case 'CC':
                if (len(line) == 3):
                    value = CalcularMiCC(inf, sup, float(line[1]), float(line[2]), x)
                    print("Cauchy: ", value)
                else:
                    print("Cauchy: Está faltando valor da forma")
            case 'GD':
                if (len(line) == 4):
                    value = CalcularMiGD(inf, sup, float(line[1]), float(line[2]), float(line[3]), x)
                    print("Gaussiana Dupla: ", value)
                else:
                    print("Gaussiana Dupla: Está faltando valor da forma")
            case 'RT':
                if (len(line) == 3):
                    value = CalcularMiRT(inf, sup, float(line[1]), float(line[2]), x)
                    print("Retangular: ", value)
                else:
                    print("Retangular: Está faltando valor da forma")
            case 'LP':
                if (len(line) == 3):
                    value = CalcularMiLP(inf, sup, float(line[1]), float(line[2]), x)
                    print("Laplace: ", value)
                else:
                    print("Laplace: Está faltando valor da forma")
    f.close()