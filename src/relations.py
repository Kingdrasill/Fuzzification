from src.operations import *
import seaborn as sns
from matplotlib.gridspec import GridSpec

# Função para calcular a relação de dois conjuntos pela função func (t-norma ou s-norma)
# do tipo tipo (value é passado para alguns tipos de func), recebe os tamanhos dos conjuntos
# e os graus de pertinência dos conjuntos
def Relacao(func, tipo, value, size_c1, size_c2, mi_c1, mi_c2):
    # Inicia a relação como uma matriz de 0s de dimensões size_c1 X size_c2
    rel = np.zeros((size_c1, size_c2))
    # Para cada pertinênci do conjunto 1
    for i in range(size_c1):
        # Para cada pertinênci do conjunto 2
        for j in range(size_c2):
            percs = [mi_c1[i], mi_c2[j]]
            # Guarda o valor da relação de cada pertinência
            rel[i][j] = func(percs, tipo, value)
    # Retorna a relação
    return rel

# Função para plotar o gráfico da relação e salvar em um arquivo
def PlotartRelacao(lim_c1, lim_c2, name_c1, name_c2, c1, c2, mi_c1, mi_c2, relation, directory, filename, name):
    fig = plt.figure(figsize=(10, 8))
    gs = GridSpec(2, 2, figure=fig)

    ax1 = fig.add_subplot(gs[0,0])
    ax2 = fig.add_subplot(gs[0,1])
    ax3 = fig.add_subplot(gs[1,:])

    # Plota o gráfico do primeiro conjunto da relação no canto superior esquerdo
    ax1.plot(c1, mi_c1)
    ax1.set_title(name_c1)
    ax1.grid(True)

    # Plota o gráfico do segundo conjunto da relação no canto superior direito
    ax2.plot(c2, mi_c2)
    ax2.set_title(name_c2)
    ax2.grid(True)

    # Plota o mapa de calor da relação ocupadando a parte de baixo dos dois gráficos superiores
    sns.heatmap(relation, ax=ax3, cmap="coolwarm", cbar=True)
    ax3.set_title(name)
    ax3.set_ylabel(name_c1)
    ax3.set_xlabel(name_c2)
    
    num_ticks_y = relation.shape[0] # Escala do primeiro conjunto
    num_ticks_x = relation.shape[1] # Escala do segundo conjunto

    y_ticks_labels = np.linspace(lim_c1[0], lim_c1[1], 15)
    x_ticks_labels = np.linspace(lim_c2[0], lim_c2[1], 15)
    
    y_ticks_labels = [f"{y:.2f}" for y in y_ticks_labels]
    x_ticks_labels = [f"{x:.2f}" for x in x_ticks_labels]

    # Seta as escalas do mapa de calor para ser as escalas das conjuntos
    ax3.set_yticks(ticks=np.linspace(0, num_ticks_y - 1, 15), labels=y_ticks_labels)
    ax3.set_xticks(ticks=np.linspace(0, num_ticks_x - 1, 15), labels=x_ticks_labels)

    plt.tight_layout()
    plt.savefig(directory + filename + ".png")
    plt.close()

# Plota a relação do conjunto Meia-Idade com o conjunto Alto, pelas t-normas ttipos e pelas s-normas stipos
def MostrarRelacao(ttipos, tvalores, tnomes, stipos, svalores, snomes, directory = "imgs/relations/"):
    # Limite do conjunto Meia-Idade
    limMeiaIdade = (25, 55)
    # Limite do conjunto Alto
    limAlto = (1.60, 1.90)

    # Amostras do conjunto Meia-Idade
    idades = np.linspace(limMeiaIdade[0], limMeiaIdade[1], 100)
    # Amostras do conjunto Alto
    alturas = np.linspace(limAlto[0], limAlto[1], 100)

    miIdade = []
    miAltura = []
    # Calcula os valors de pertinência do conjunto Meia-Idade
    for i in idades:
        miIdade.append(CalcularMiSN(limMeiaIdade[0], limMeiaIdade[1], 6, 2.5, 40, i))
    # Calcula os valors de pertinência do conjunto Alto
    for a in alturas:
        miAltura.append(CalcularMiTR(limAlto[0], limAlto[1], 1.60, 1.90, 1.90, a))

    # Para cada tipo de T-norma gera a relação dos conjuntos Meia-Idade e Alto, salvando em um arquivo
    for i in range(len(ttipos)):
        relacao = Relacao(TNorma, ttipos[i], tvalores[i], len(miIdade), len(miAltura), miIdade, miAltura)
        PlotartRelacao(limMeiaIdade, limAlto, "Conjunto Meia-Idade", "Conjunto Alto", idades, alturas, miIdade, miAltura, relacao, directory, "relacao-TNorma-"+ttipos[i], "Pessoas Altas e de Meia-Idade (T-Norma {})".format(tnomes[i]))
   
    # Para cada tipo de S-norma gera a relação dos conjuntos Meia-Idade e Alto, salvando em um arquivo
    for i in range(len(stipos)):
        relacao = Relacao(SNorma, stipos[i], svalores[i], len(miIdade), len(miAltura), miIdade, miAltura)
        PlotartRelacao(limMeiaIdade, limAlto, "Conjunto Meia-Idade", "Conjunto Alto", idades, alturas, miIdade, miAltura, relacao, directory, "relacao-SNorma-"+stipos[i], "Pessoas Altas ou de Meia-Idade (S-Norma {})".format(snomes[i]))