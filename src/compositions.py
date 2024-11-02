from src.relations import *

def Composicao(r1, r2, tipo):
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

def PlotarComposicao(u, v, w, relacao_uv, name_uv, relacao_vw, name_vw, composicao, name_composicao, filename, directory):
    fig = plt.figure(figsize=(10, 8))
    gs = GridSpec(2, 2, figure=fig)
    ax1 = fig.add_subplot(gs[0,0])
    ax2 = fig.add_subplot(gs[0,1])
    ax3 = fig.add_subplot(gs[1,:])

    # Plot relação u-v
    sns.heatmap(relacao_uv, annot=True, cmap="coolwarm", cbar=True, ax=ax1)
    ax1.set_title(name_uv)
    ax1.set_xlabel("V")
    ax1.set_ylabel("U")
    ax1.set_xticks([(x+0.5) for x in range(len(v))])
    ax1.set_yticks([(x+0.5) for x in range(len(u))])
    ax1.set_xticklabels(v)
    ax1.set_yticklabels(u)

    # Plot relação v-w
    sns.heatmap(relacao_vw, annot=True, cmap="coolwarm", cbar=True, ax=ax2)
    ax2.set_title(name_vw)
    ax2.set_xlabel("W")
    ax2.set_ylabel("V")
    ax2.set_xticks([(x+0.5) for x in range(len(w))])
    ax2.set_yticks([(x+0.5) for x in range(len(v))])
    ax2.set_xticklabels(w)
    ax2.set_yticklabels(v)

    # Plot composição u-w
    sns.heatmap(composicao, annot=True, cmap="coolwarm", cbar=True, ax=ax3)
    ax3.set_title(name_composicao)
    ax3.set_xlabel("W")
    ax3.set_ylabel("U")
    ax3.set_xticks([(x+0.5) for x in range(len(w))])
    ax3.set_yticks([(x+0.5) for x in range(len(u))])
    ax3.set_xticklabels(w)
    ax3.set_yticklabels(u)

    plt.tight_layout()
    plt.savefig(directory + filename + ".png")
    plt.close()

def MostrarComposicao(directory = "imgs/compositions/"):
    u = [2, 12]
    v = [1, 7, 13]
    w = [4, 8]

    relacao_uv = [[0.9, 0.4, 0.1], [0.1, 0.4, 0.9]] # u é próximo de v
    relacao_vw = [[0, 0], [0.6, 0], [1, 0.7]]       # v é muito mair que w

    for cmp in ["Max-Min", "Min-Max", "Max-Prod"]:
        composicao = Composicao(relacao_uv, relacao_vw, cmp)
        PlotarComposicao(u, v, w, relacao_uv, "Relação (u,v): u é próximo de v", 
                            relacao_vw, "Relação (v,w): v é muito maior que w", 
                            composicao, "Composição (u,w)" + cmp, "composicao-" + cmp.lower(), directory)
