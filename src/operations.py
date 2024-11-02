from src.domain import *
from functools import reduce

def Complemento(domain, x):
    complements = []
    for i in range(len(domain.funcs)):
        complements.append([])
    for i in x:
        graus = domain.calcularGrauAtivacao(i)
        for j in range(len(graus)):
            complements[j].append(1 - graus[j])
    return complements

def Uniao(domain, x):
    union = []
    for i in x:
        graus = domain.calcularGrauAtivacao(i)
        union.append(max(graus))
    return union

def Intersercao(domain, x):
    intersection = []
    for i in x:
        graus = domain.calcularGrauAtivacao(i)
        intersection.append(min(graus))
    return intersection

def TNorma(graus, tipo, value=0):
    match tipo:
        case "M":
            return min(graus)
        case "P":
            return reduce(lambda acc, x: acc * x, graus, 1)
        case "L":
            if value < -1:
                return None
            sum_graus = np.sum(graus)
            prod_graus = np.prod(graus)
            return (max(0, (1 + value) * (sum_graus - (len(graus) - 1)) - value * prod_graus))
        case "H":
            if value < 0:
                return None
            sum_graus = np.sum(graus) 
            prod_graus = np.prod(graus)
            den = value + (1 - value) * (sum_graus - prod_graus)
            if den == 0:
                return None
            return (prod_graus / den)
        case "D":
            sum_graus = np.sum(graus) 
            return (max(sum_graus - (len(graus) - 1), 0))
        case "W":
            non_one = [v for v in graus if v != 1]
            if len(non_one) == 1:
                return non_one[0]
            else:
                return 0
    return None

def SNorma(graus, tipo, value=0):
    match tipo:
        case "M":
            return max(graus)
        case "P":
            sum_graus = np.sum(graus)
            prod_graus = np.prod(graus)
            return (sum_graus - prod_graus)
        case "L":
            if value < 0:
                return None
            sum_graus = np.sum(graus)
            prod_graus = np.prod(graus)
            return (min(1, sum_graus + value * prod_graus))
        case "H":
            if value < 0:
                return None
            sum_graus = np.sum(graus) 
            prod_graus = np.prod(graus)
            num = sum_graus - prod_graus - (1 - value) * prod_graus
            den = 1 - (1 - value) * prod_graus
            if den == 0:
                return None
            return (num / den)
        case "S":
            sum_graus = np.sum(graus) 
            return (min(sum_graus, 1))
        case "W":
            non_zero = [v for v in graus if v != 0]
            if len(non_zero) == 1:
                return non_zero[0]
            else:
                return 1
    return None

def MostrarOpercacoes(domains, directory = "imgs/operations/"):
    for domain in domains:
        fig, ax = plt.subplots(2, 3, figsize=(12, 9))

        x = np.linspace(domain.inf, domain.sup, 500)
        for f in domain.funcs:
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
            ax[0, 0].plot(x, y)
        ax[0, 0].set_title(domain.name)
        ax[0, 0].grid(True)

        cs = Complemento(domain, x)
        for f in cs:
            ax[1, 0].plot(x, f)
        ax[1, 0].set_title("Complementos")
        ax[1, 0].grid(True)

        u = Uniao(domain, x)
        ax[0, 1].plot(x, u, color="red")
        ax[0, 1].set_title("União")
        ax[0, 1].grid(True)

        s = []
        for a in x:
            graus = domain.calcularGrauAtivacao(a)
            snorm = SNorma(graus, "P")
            if snorm == None:
                s = None
                break
            s.append(snorm)
        if s != None:
            ax[1, 1].plot(x, s, color="green")
            ax[1, 1].set_title("S-norma Soma Probabilística")
            ax[1, 1].grid(True)


        i = Intersercao(domain, x)
        ax[0, 2].plot(x, i, color="blue")
        ax[0, 2].set_title("Interseção")
        ax[0, 2].grid(True)

        t = []
        for a in x:
            graus = domain.calcularGrauAtivacao(a)
            tnorm = TNorma(graus, "P")
            if tnorm == None:
                t = None
                break
            t.append(tnorm)
        if t != None:
            ax[1, 2].plot(x, t, color="purple")
            ax[1, 2].set_title("T-norma Produto Algébrico")
            ax[1, 2].grid(True)
        
        plt.tight_layout()
        plt.savefig(directory + domain.name + ".png")