from operations import *
import seaborn as sns
from matplotlib.gridspec import GridSpec

def relation(func, tipo, value, size_c1, size_c2, perc_c1, perc_c2):
    rel = np.zeros((size_c1, size_c2))
    for i in range(size_c1):
        for j in range(size_c2):
            percs = [perc_c1[i], perc_c2[j]]
            rel[i][j] = func(percs, tipo, value)
    return rel

def save_relation_to_file(x, c1name, c2name, c1, c2, c1lim, c2lim, relation_matrix, tipo, filename, directory):
    fig = plt.figure(figsize=(10, 8))
    gs = GridSpec(2, 2, figure=fig)

    ax1 = fig.add_subplot(gs[0,0])
    ax2 = fig.add_subplot(gs[0,1])
    ax3 = fig.add_subplot(gs[1,0:1])

    ax1.plot(x, c1, color="red")
    ax1.set_title(c1name)
    ax1.grid(True)

    ax2.plot(x, c2, color="blue")
    ax2.set_title(c2name)
    ax2.grid(True)

    sns.heatmap(relation_matrix, cmap="coolwarm", cbar=True)

    ax3.set_title(tipo)
    ax3.set_xlabel(c2name)
    ax3.set_ylabel(c1name)

    num_ticks_x = relation_matrix.shape[1]
    num_ticks_y = relation_matrix.shape[0]
    
    xticks_labels = np.linspace(c2lim[0], c2lim[1], 10)
    yticks_labels = np.linspace(c1lim[0], c1lim[1], 10)

    xticks_labels = [f"{x:.2f}" for x in xticks_labels]
    yticks_labels = [f"{y:.2f}" for y in yticks_labels]

    ax3.set_xticks(ticks=np.linspace(0, num_ticks_x - 1, 10), labels=xticks_labels)
    ax3.set_yticks(ticks=np.linspace(0, num_ticks_y - 1, 10), labels=yticks_labels)

    plt.tight_layout()
    plt.savefig(directory + filename + ".png")
    plt.close()

def MostrarRelacao(directory = "data/imgs/relations/"):
    inf = 0
    sup = 10

    c1_values = (0, 4, 6, 10)
    c1name = "Trapezoidal"
    c2_values = (1, 5)
    c2name = "S-shaped"

    x = np.linspace(inf, sup, 250)
    percs_c1, percs_c2 = [], []
    for i in x:
        percs_c1.append(CalcularMiTP(inf, sup, c1_values[0], c1_values[1], c1_values[2], c1_values[3], i))
        percs_c2.append(CalcularMiSS(inf, sup, c2_values[0], c2_values[1], i))

    r1 = relation(TNorma, "M", None, len(percs_c1), len(percs_c2), percs_c1, percs_c2)
    r2 = relation(TNorma, "P", None, len(percs_c1), len(percs_c2), percs_c1, percs_c2)
    r3 = relation(SNorma, "M", None, len(percs_c1), len(percs_c2), percs_c1, percs_c2)
    r4 = relation(SNorma, "P", None, len(percs_c1), len(percs_c2), percs_c1, percs_c2)

    save_relation_to_file(x, c1name, c2name, percs_c1, percs_c2, (0, 10), (0, 10), r1, "T-norma Min Zadeh", "relation-tnorma-min", directory)
    save_relation_to_file(x, c1name, c2name, percs_c1, percs_c2, (0, 10), (0, 10), r2, "T-norma Produto Algébrico", "relation-tnorma-prd", directory)
    save_relation_to_file(x, c1name, c2name, percs_c1, percs_c2, (0, 10), (0, 10), r3, "T-norma Max Zadeh", "relation-snorma-max", directory)
    save_relation_to_file(x, c1name, c2name, percs_c1, percs_c2, (0, 10), (0, 10), r4, "T-norma Soma Probabilística", "relation-snorma-sum", directory)