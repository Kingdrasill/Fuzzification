from relations import *

def composition(r1, r2, tipo):
    s_l_r1 = len(r1)
    s_c_r2 = len(r2[0])

    if s_l_r1 != s_c_r2:
        return None

    comp = np.zeros((s_l_r1, s_c_r2))

    match tipo:
        case "Max-Min":
            for i in range(s_l_r1):
                for j in range(s_c_r2):
                    l_r1 = r1[i]
                    c_r2 = [row[j] for row in r2]
                    minimos = []
                    for v1, v2, in zip(l_r1, c_r2):
                        minimos.append(min(v1, v2))
                    comp[i][j] = max(minimos)
        case "Min-Max":
            for i in range(s_l_r1):
                for j in range(s_c_r2):
                    l_r1 = r1[i]
                    c_r2 = [row[j] for row in r2]
                    minimos = []
                    for v1, v2, in zip(l_r1, c_r2):
                        minimos.append(max(v1, v2))
                    comp[i][j] = min(minimos)
        case "Max-Prod":
            for i in range(s_l_r1):
                for j in range(s_c_r2):
                    l_r1 = r1[i]
                    c_r2 = [row[j] for row in r2]
                    prods = []
                    for v1, v2, in zip(l_r1, c_r2):
                        prods.append(v1 * v2)
                    comp[i][j] = max(prods)
    return comp

def save_composition_to_file(x, c1name, c2name, c3name, c1, c2, c3, c1lim, c3lim, composition, tipo, filename, directory):
    fig = plt.figure(figsize=(10, 8))
    gs = GridSpec(2, 2, figure=fig)

    ax1 = fig.add_subplot(gs[0,0])
    ax2 = fig.add_subplot(gs[0,1])
    ax3 = fig.add_subplot(gs[1,0])
    ax4 = fig.add_subplot(gs[1,1])

    ax1.plot(x, c1, color="red")
    ax1.set_title(c1name)
    ax1.grid(True)

    ax2.plot(x, c2, color="blue")
    ax2.set_title(c2name)
    ax2.grid(True)

    ax3.plot(x, c3, color="green")
    ax3.set_title(c3name)
    ax3.grid(True)

    sns.heatmap(composition, cmap="coolwarm", cbar=True)

    ax4.set_title("Composição " + tipo + " da " + c1name + " e " + c3name)
    ax4.set_xlabel(c3name)
    ax4.set_ylabel(c1name)

    num_ticks_x = composition.shape[1]
    num_ticks_y = composition.shape[0]
    
    xticks_labels = np.linspace(c3lim[0], c3lim[1], 10)
    yticks_labels = np.linspace(c1lim[0], c1lim[1], 10)

    xticks_labels = [f"{x:.2f}" for x in xticks_labels]
    yticks_labels = [f"{y:.2f}" for y in yticks_labels]

    ax4.set_xticks(ticks=np.linspace(0, num_ticks_x - 1, 10), labels=xticks_labels)
    ax4.set_yticks(ticks=np.linspace(0, num_ticks_y - 1, 10), labels=yticks_labels)

    plt.tight_layout()
    plt.savefig(directory + filename + ".png")
    plt.close()

def MostrarComposicao(directory = "data/imgs/compositions/"):
    inf = 0
    sup = 10

    c1_values = (5, 2)
    c1name = "Gaussiana"
    c2_values = (2, 3, 4)
    c2name = "Sino"
    c3_values = (3, 1)
    c3name = "Laplace"

    x = np.linspace(inf, sup, 250)
    percs_c1, percs_c2, percs_c3 = [], [], []
    for i in x:
        percs_c1.append(CalcularMiGS(inf, sup, c1_values[0], c1_values[1], i))
        percs_c2.append(CalcularMiSN(inf, sup, c2_values[0], c2_values[1], c2_values[2], i))
        percs_c3.append(CalcularMiLP(inf, sup, c3_values[0], c3_values[1], i))

    r1 = relation(TNorma, "M", None, len(percs_c1), len(percs_c2), percs_c1, percs_c2)
    r2 = relation(SNorma, "M", None, len(percs_c2), len(percs_c3), percs_c2, percs_c3)

    for comp in ["Max-Min", "Min-Max", "Max-Prod"]:
        cmp = composition(r1, r2, comp)

        save_composition_to_file(x, c1name, c2name, c3name, percs_c1, percs_c2, percs_c3, (inf, sup), (inf, sup), cmp, comp, ("compostion-"+comp.lower()), directory)

AcharGrauPertinência()
domains = AcharGrauAtivacaoFuncoes()
MostrarOpercacoes(domains)
MostrarRelacao()
MostrarComposicao()