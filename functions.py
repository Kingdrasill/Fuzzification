import math

class Triangular:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Triangular"

    def setValues(self, a, b, c):
        if a > b or c < b:
            return False
        self.a = a
        self.b = b
        self.c = c
        return True

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        if (x <= self.a):
            return 0
        elif (x > self.a and x <= self.b):
            return ((x - self.a)/(self.b - self.a))
        elif (x > self.b and x <= self.c):
            return ((self.c - x)/(self.c - self.b))
        elif (x > self.c):
            return 0

class Trapezoidal:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Trapezoidal"

    def setValues(self, a, b, c, d):
        if a > b or b > c or c > d:
            return False
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        return True 

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        if (x <= self.a):
            return 0
        elif (x > self.a and x <= self.b):
            return ((x - self.a)/(self.b - self.a))
        elif (x > self.b and x <= self.c):
            return 1
        elif (x > self.c and x <= self.d):
            return ((self.d - x)/(self.d - self.c))
        elif (x > self.d):
            return 0

class Gaussiana:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Gaussiana"

    def setValues(self, c, sigma):
        self.c = c
        self.sigma = sigma

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        return math.exp(-((x - self.c) ** 2)/(2 * self.sigma ** 2))

class Sigmoidal:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Sigmoidal"

    def setValues(self, a, c):
        self.a = a
        self.c = c

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        return (1 / (1 + math.exp(((-self.a) * (x - self.c)))))

class Sino:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Sino"

    def setValues(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        return (1 / (1 + (abs((x - self.c)/self.a)**(2 * self.b))))

class Sshaped:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "S-shaped"

    def setValues(self, a, b):
        self.a = a
        self.b = b

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        if (x <= self.a):
            return 0
        elif (x > self.a and x <= ((self.a + self.b)/2)):
            return (2*(((x - self.a)/(self.b - self.a))**2))
        elif (x > ((self.a + self.b)/2) and x <= self.b):
            return (1 - 2 * (((self.b - x)/(self.b - self.a))**2))
        elif (x > self.b):
            return 1

class Zshaped:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Z-shaped"

    def setValues(self, a, b):
        self.a = a
        self.b = b

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        if (x <= self.a):
            return 1
        elif (x > self.a and x <= ((self.a + self.b)/2)):
            return (1 - 2 * (((x - self.a)/(self.b - self.a))**2))
        elif (x > ((self.a + self.b)/2) and x <= self.b):
            return (2*(((self.b - x)/(self.b - self.a))**2))
        elif (x > self.b):
            return 0

class Cauchy:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Cauchy"

    def setValues(self, x_0, gamma):
        self.x_0 = x_0
        self.gamma = gamma

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        return (1/((math.pi * self.gamma) * (1 + ((x - self.x_0)/self.gamma) ** 2)))
    
class GaussianaDupla:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Gaussiana Dupla"

    def setValues(self, mi, sigma1, sigma2):
        self.mi = mi
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.A = math.sqrt(2/math.pi)*(self.sigma1+self.sigma2)**(-1)

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        if (x < self.mi):
            return (self.A * math.exp(-((x - self.mi)**2/(2*(self.sigma1**2)))))
        else:
            return (self.A * math.exp(-((x - self.mi)**2/(2*(self.sigma2**2)))))

class Retangular:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Retangular"

    def setValues(self, a, b):
        self.a = a
        self.b = b

    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        if (x >= self.a and x <= self.b):
            return 1
        else:
            return 0

class Laplace:
    def __init__(self, inferior, superior):
        self.inf = inferior
        self.sup = superior
        self.name = "Laplace"

    def setValues(self, mi, b):
        self.mi = mi
        self.b = b
    
    def calcularMi(self, x):
        if (x < self.inf or x > self.sup):
            return None
        return ((1 / (2 * self.b)) * math.exp(- (abs(x - self.mi)) / self.b))

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
                func = Triangular(inf, sup)
                func.setValues(float(line[1]), float(line[2]), float(line[3]))
                print("Triangular: ", func.calcularMi(x))
            case 'TP':
                func = Trapezoidal(inf, sup)
                func.setValues(float(line[1]), float(line[2]), float(line[3]), float(line[4]))
                print("Trapezoidal: ", func.calcularMi(x))
            case 'GS':
                func = Gaussiana(inf, sup)
                func.setValues(float(line[1]), float(line[2]))
                print("Gaussiana: ", func.calcularMi(x))
            case 'SG':
                func = Sigmoidal(inf, sup)
                func.setValues(float(line[1]), float(line[2]))
                print("Sigmoidal: ", func.calcularMi(x))
            case 'SN':
                func = Sino(inf, sup)
                func.setValues(float(line[1]), float(line[2]), float(line[3]))
                print("Sino: ", func.calcularMi(x))
            case 'SS':
                func = Sshaped(inf, sup)
                func.setValues(float(line[1]), float(line[2]))
                print("S-shaped: ", func.calcularMi(x))
            case 'ZS':
                func = Zshaped(inf, sup)
                func.setValues(float(line[1]), float(line[2]))
                print("Z-shaped: ", func.calcularMi(x))
            case 'CC':
                func = Cauchy(inf, sup)
                func.setValues(float(line[1]), float(line[2]))
                print("Cauchy: ", func.calcularMi(x))
            case 'GD':
                func = GaussianaDupla(inf, sup)
                func.setValues(float(line[1]), float(line[2]), float(line[3]))
                print("Gaussiana Dupla: ", func.calcularMi(x))
            case 'RT':
                func = Retangular(inf, sup)
                func.setValues(float(line[1]), float(line[2]))
                print("Retangular : ", func.calcularMi(x))
            case 'LP':
                func = Laplace(inf, sup)
                func.setValues(float(line[1]), float(line[2]))
                print("Laplace: ", func.calcularMi(x))
    f.close()