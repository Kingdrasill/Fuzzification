from src.operations import *
import seaborn as sns
from matplotlib.gridspec import GridSpec

def Relacao(func, tipo, value, size_c1, size_c2, mi_c1, mi_c2):
    rel = np.zeros((size_c1, size_c2))
    for i in range(size_c1):
        for j in range(size_c2):
            percs = [mi_c1[i], mi_c2[j]]
            rel[i][j] = func(percs, tipo, value)
    return rel

def PlotartRelacao(lim_c1, lim_c2, name_c1, name_c2, c1, c2, mi_c1, mi_c2, relation, directory, filename, name):
    fig = plt.figure(figsize=(10, 8))
    gs = GridSpec(2, 2, figure=fig)

    ax1 = fig.add_subplot(gs[0,0])
    ax2 = fig.add_subplot(gs[0,1])
    ax3 = fig.add_subplot(gs[1,:])

    ax1.plot(c1, mi_c1)
    ax1.set_title(name_c1)
    ax1.grid(True)

    ax2.plot(c2, mi_c2)
    ax2.set_title(name_c2)
    ax2.grid(True)

    sns.heatmap(relation, ax=ax3, cmap="coolwarm", cbar=True)
    ax3.set_title(name)
    ax3.set_ylabel(name_c1)
    ax3.set_xlabel(name_c2)
    
    num_ticks_y = relation.shape[0] # Escala de C1
    num_ticks_x = relation.shape[1] # Escala de C2

    y_ticks_labels = np.linspace(lim_c1[0], lim_c1[1], 15)
    x_ticks_labels = np.linspace(lim_c2[0], lim_c2[1], 15)
    
    y_ticks_labels = [f"{y:.2f}" for y in y_ticks_labels]
    x_ticks_labels = [f"{x:.2f}" for x in x_ticks_labels]

    ax3.set_yticks(ticks=np.linspace(0, num_ticks_y - 1, 15), labels=y_ticks_labels)
    ax3.set_xticks(ticks=np.linspace(0, num_ticks_x - 1, 15), labels=x_ticks_labels)

    plt.tight_layout()
    plt.savefig(directory + filename + ".png")
    plt.close()

def MostrarRelacao(ttipos, tvalores, tnomes, stipos, svalores, snomes, directory = "imgs/relations/"):
    limMeiaIdade = (25, 55)
    limAlto = (1.60, 1.90)

    idades = np.linspace(limMeiaIdade[0], limMeiaIdade[1], 100)
    alturas = np.linspace(limAlto[0], limAlto[1], 100)

    miIdade = []
    miAltura = []
    for i in idades:
        miIdade.append(CalcularMiSN(limMeiaIdade[0], limMeiaIdade[1], 6, 2.5, 40, i))
    for a in alturas:
        miAltura.append(CalcularMiTR(limAlto[0], limAlto[1], 1.60, 1.90, 1.90, a))

    for i in range(len(ttipos)):
        relacao = Relacao(TNorma, ttipos[i], tvalores[i], len(miIdade), len(miAltura), miIdade, miAltura)
        PlotartRelacao(limMeiaIdade, limAlto, "Conjunto Meia-Idade", "Conjunto Alto", idades, alturas, miIdade, miAltura, relacao, directory, "relacao-TNorma-"+ttipos[i], "Pessoas Altas e de Meia-Idade (T-Norma {})".format(tnomes[i]))
   
    for i in range(len(stipos)):
        relacao = Relacao(SNorma, stipos[i], svalores[i], len(miIdade), len(miAltura), miIdade, miAltura)
        PlotartRelacao(limMeiaIdade, limAlto, "Conjunto Meia-Idade", "Conjunto Alto", idades, alturas, miIdade, miAltura, relacao, directory, "relacao-SNorma-"+stipos[i], "Pessoas Altas ou de Meia-Idade (S-Norma {})".format(snomes[i]))