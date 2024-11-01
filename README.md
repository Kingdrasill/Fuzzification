<div style="display: none;">
  <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" }); </script>
</div>

<div style="text-align: justify;">

# Conjuntos, Funções e Operadores Fuzzy

## Gabriel Teixeira Júlio

## Execução

Para executar o código, basta rodar o arquivo `main.py`. Isso abrirá um menu com as opções disponíveis para os testes.

# Questão 1

**Implemente uma função para calcular a pertinência de um valor em uma função de pertinência:**

- **Triangular**
- **Trapezoidal**
- **Gaussiana**
- **Sigmoidal**
- **Sino**
- **S**
- **Z**
- **Cauchy**
- **Gaussiana Dupla**
- **Retangular**
- **Laplace**

## Implementação

Todas as funções implementadas recebem os seguintes parâmetros:

- **inf** - Limite inferior da função
- **sup** - Limite superior da função
- **constantes** - Valores específicos de cada tipo de função, utilizados para definir sua forma
- **x** - Valor para o qual será calculado o grau de pertinência

### Função Triangular

Além dos valores comuns entre as outras funções, esta função recebe as constantes **a**, **b** e **c**, que definem a forma do triângulo.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/1.jpg)

### Função Trapezoidal

Além dos valores comuns entre as outras funções, esta função recebe as constantes **a**, **b**, **c** e **d**, que definem a forma do trapézio.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/2.jpg)

### Função Gaussiana

Além dos valores comuns entre as outras funções, esta função recebe as constantes **c**, que é o centro da curva, e **$\sigma$**, que é o desvio padrão que controla a largura.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/3.jpg)

### Função Sigmoidal

Além dos valores comuns entre as outras funções, esta função recebe as constantes **a**, que controla a inclinação, e **c**, que é a posição central.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/4.jpg)

### Função Sino

Além dos valores comuns entre as outras funções, esta função recebe as constantes **a**, que controla a largura, **b**, que controla a suavidade, e **c**, que é o ponto central.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/5.jpg)

### Função S

Além dos valores comuns entre as outras funções, esta função recebe as constantes **a** e **b**, que são os pontos de controle da função.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/6.jpg)

### Função Z

Além dos valores comuns entre as outras funções, esta função recebe as constantes **a** e **b**, que são os pontos de controle da função.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/7.jpg)

### Função Cauchy

Além dos valores comuns entre as outras funções, esta função recebe as constantes **x₀**, o parâmetro de localização que especifica o pico da distribuição, e **$\gamma$**, o parâmetro de escala.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/8.jpg)

### Função Gaussiana Dupla

Além dos valores comuns entre as outras funções, esta função recebe as constantes **$\mu$**, que define o centro, **$\sigma₁$** para a distribuição do lado esquerdo, e **$\sigma₂$** para a distribuição do lado direito.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/9.jpg)

### Função Retangular

Além dos valores comuns entre as outras funções, esta função recebe as constantes **a**, o limite inferior onde a pertinência é 1, e **b**, o limite superior onde a pertinência é 1.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/10.jpg)

### Função Laplace

Além dos valores comuns entre as outras funções, esta função recebe as constantes **$\mu$**, o parâmetro de localização do centro, e **b**, o parâmetro de escala.

O valor de **x** passado para a função é calculado pela seguinte fórmula:

![alt text](data/equations/11.jpg)
## Teste

Para testar o uso das funções, foi criado um método que lê de um arquivo *txt* as funções a serem testadas e seus parâmetros. Em seguida, é calculado o grau de pertinência para um valor informado pelo usuário.

Abaixo estão os graus de pertinência para **x = 2.89** em cada uma das funções implementadas, com seus respectivos parâmetros:

- **Triangular [a=3, b=6, c=8]**:
  - Grau de pertinência de 2.89: **0.0**
- **Trapezoidal [a=1, b=5, c=7, d=8]**:
  - Grau de pertinência de 2.89: **0.4725**
- **Gaussiana [c=5, $\sigma$=2]**:
  - Grau de pertinência de 2.89: **0.5732**
- **Sigmoidal [a=2, c=4]**:
  - Grau de pertinência de 2.89: **0.0980**
- **Sino [a=2, b=4, c=6]**:
  - Grau de pertinência de 2.89: **0.1458**
- **S-shaped [a=1, b=8]**:
  - Grau de pertinência de 2.89: **1.0**
- **Z-shaped [a=3, b=7]**:
  - Grau de pertinência de 2.89: **0.0466**
- **Cauchy [$x_0$=6, $\gamma$=2]**:
  - Grau de pertinência de 2.89: **0.0780**
- **Gaussiana Dupla [$\mu$=7, $\sigma_1$=3, $\sigma_2$=1]**:
  - Grau de pertinência de 2.89: **0.0780**
- **Retangular [a=2, b=6]**:
  - Grau de pertinência de 2.89: **1.0**
- **Laplace [$\mu$=4, b=3]**:
  - Grau de pertinência de 2.89: **0.1151**

<br><br>

# Questão 2

**Defina o domínio (universo de discurso) para uma variável de entrada a sua escolha. Particione esse universo de discurso em no mínimo 4 funções de pertinência uniformemente espac¸adas. Realize a fuzzificac¸ao (calculo do grau de ativação das funções) para duas amostras considerando cada uma das funções apresentadas na atividade anterior. Apresente uma análise gráfica e textual comparativa dos resultados obtidos.**

## Implementação

Foi criada uma classe para representar o domínio de uma variável de entrada fuzzy. A classe armazena os seguintes dados:

- **inf**: limite inferior do domínio
- **sup**: limite superior do domínio
- **funcs**: funções dentro do domínio
- **name**: nome do domínio

A variável **funcs** é um dicionário que armazena as seguintes informações das funções do domínio:

- **tipo**: tipo de função, entre as implementadas na seção anterior
- **func**: método que deve ser chamado para calcular o grau de ativação para um valor
- **values**: vetor com os valores de limite e forma que serão passados para **func**

A classe também possui dois métodos:

- **calcularGrauAtivacao**: recebe um valor **x** e calcula o grau de ativação de **x** nas funções armazenadas em **funcs** da classe.
- **plotarGrauAtivacao**: recebe dois valores **x1** e **x2**, e o diretório onde o gráfico deve ser armazenado. Este método plota um gráfico com todas as funções no domínio e inclui duas retas verticais tracejadas, indicando os pontos onde as funções são cortadas nos valores **x1** e **x2**.

## Teste

Foi criada uma função para gerar domínios para todas as funções implementadas na seção anterior.

Primeiro, é sorteado um número entre 4 e 6, que define o número de funções dentro do domínio; em seguida, o usuário fornece os valores das duas amostras.

Com esses valores, as funções do domínio são geradas aleatoriamente e distribuídas de forma uniforme. Após a geração das funções do domínio, é utilizado o método **plotarGrauAtivacao** para gerar o gráfico do domínio e salvá-lo em um arquivo.

A seguir, estão os gráficos gerados para todos os tipos de funções, considerando as amostras **x1=2.89** e **x2=8.97**.

Todos os gráfio abaixo mostram o domínio de uma variável fuzzy com limites de 0 a 10, contendo 4 funções de pertinência uniformemente distribuídas. As funções são diferenciadas pelas cores: azul, laranja, verde e vermelha. Além disso as duas retas verticais tracejadas (roxa e preta) representam as amostras.

### Domínio Triangular

<img src="data/imgs/domains/Triangular.png">

O gráfico acima apresenta funções triangulares, onde o maior grau de ativação possível para qualquer valor de amostra é 1 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa todas funções do domínio , na seguinte ordem de grau de ativação: **azul > laranja > vermelha > verde**.

A amostra **x = 8.97** (reta preta) ativa as funções laranja, verde e vermelha, na seguinte ordem de grau de ativação: **verde > vermelha > laranja**. A amostra não ativa a função azul.

<br><br><br><br><br><br><br><br><br><br>

### Domínio Trapezoidal

<img src="data/imgs/domains/Trapezoidal.png">

O gráfico acima apresenta funções trapezoidais, onde o maior grau de ativação possível para qualquer valor de amostra é 1 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa as funções azul, verde e vermelha, com a ordem decrescente de grau de ativação: **azul > vermelha > verde**. A amostra não ativa a função laranja.

A amostra **x = 8.97** (reta preta) ativa as funções verde e vermelha, na seguinte ordem de grau de ativação: **vermelha > verde**. A amostra não ativa as funções azul e laranja.

<br><br><br><br><br><br><br><br><br><br>

### Domínio Gaussiana

<img src="data/imgs/domains/Gaussiana.png">

O gráfico acima apresenta funções gaussianas, onde o maior grau de ativação possível para qualquer valor de amostra é 1 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa todas funções do domínio, na seguinte ordem de grau de ativação: **laranja > verde > vermelha > azul**. 

A amostra **x = 8.97** (reta preta) ativa as funções verde e vermelha, na seguinte ordem de grau de ativação: **verde > vermelha**. A amostra não ativa as funções azul e laranja.

<br><br><br><br><br><br><br><br><br><br>

### Domínio Sigmoidal

<img src="data/imgs/domains/Sigmoidal.png">

O gráfico acima apresenta funções sigmodais, onde o maior grau de ativação possível para qualquer valor de amostra é 1 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa as funções azul e laranja, na seguinte ordem de grau de ativação: **azul > laranja**. A amostra não ativa as funções verde e vermelha.

A amostra **x = 8.97** (reta preta) ativa as funções azul, laranja e verde, na seguinte ordem de grau de ativação: **azul = laranja = verde**. A amostra não ativa a função vermelha.

<br><br><br><br><br><br><br><br><br><br>

### Domínio Sino

<img src="data/imgs/domains/Sino.png">

O gráfico acima apresenta funções sinos, onde o maior grau de ativação possível para qualquer valor de amostra é 1 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa todas as funções do domínio, na seguinte ordem de grau de ativação: **azul > laranja > verde > vermelha**.

A amostra **x = 8.97** (reta preta) ativa todas as funções do domínio, na seguinte ordem de grau de ativação: **vermelha > verde > laranja > azul**.

<br><br><br><br><br><br><br><br><br><br>

### Domínio S

<img src="data/imgs/domains/S-shaped.png">

O gráfico acima apresenta funções S-shapeds, onde o maior grau de ativação possível para qualquer valor de amostra é 1 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa apenas a função azul. A amostra não ativa as funções laranja, verde e vermelha.

A amostra **x = 8.97** (reta preta) ativa todas funções do domínio, na seguinte ordem de grau de ativação: **azul = laranja = verde > vermelha**.

<br><br><br><br><br><br><br><br><br><br>

### Domínio Z

<img src="data/imgs/domains/Z-shaped.png">

O gráfico acima apresenta funções Z-shapeds, onde o maior grau de ativação possível para qualquer valor de amostra é 1 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa as funções laranja, verde e vermelha, na seguinte ordem de grau de ativação: **laranja = verde = vermelha**. A amostra não ativa a função azul.

A amostra **x = 8.97** (reta preta) ativa apenas a função vermelha. A amostra não ativa as funções azul, laranja e verde.

<br><br><br><br><br><br><br><br><br><br>

### Domínio Cauchy

<img src="data/imgs/domains/Cauchy.png">

O gráfico acima apresenta funções cauchys, onde o maior grau de ativação possível para qualquer valor de amostra é 0.2027 para qualquer função.

A amostra **x = 2.89** (reta roxa) todas funções do domínio, na seguinte ordem de grau de ativação: **azul > laranja > verde > vermelha**.

A amostra **x = 8.97** (reta preta) todas funções do domínio, na seguinte ordem de grau de ativação: **verde > vermelha > laranja > azul**.

<br><br><br><br><br><br><br><br><br><br>

### Domínio Gaussiana Dupla

<img src="data/imgs/domains/Gaussiana Dupla.png">

O gráfico acima apresenta funções guassianas dupla, onde o maior grau de ativação possível para qualquer valor de amostra é 0.159 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa todas as funções do domínio, na seguinte ordem de grau de ativação: **azul > laranja > vermelha > verde**.

A amostra **x = 8.97** (reta preta) ativa as funções laranja, verde e vermelha, na seguinte ordem de grau de ativação: **vermelha > verde > laranja**. A amostra não ativa a função azul.

<br><br><br><br><br><br><br><br><br><br>

### Domínio Retangular

<img src="data/imgs/domains/Retangular.png">

O gráfico acima apresenta funções retangulares, onde o maior grau de ativação possível para qualquer valor de amostra é 1 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa as funções azul e laranaja, na seguinte ordem de grau de ativação: azul = laranja. A amostra não ativa as funções verde e, vermelha.

A amostra **x = 8.97** (reta preta) ativa apenas a função veremlha. A amostra não ativa as funções azul, laranja e verde.

<br><br><br><br><br><br><br><br><br><br>

### Domínio Laplace

<img src="data/imgs/domains/Laplace.png">

O gráfico acima apresenta funções retangulares, onde o maior grau de ativação possível para qualquer valor de amostra é 0.55 para qualquer função.

A amostra **x = 2.89** (reta roxa) ativa as funções azul, laranja e verde, na seguinte ordem de grau de ativação: **laranja > azul > verde**. A amostra não ativa a função vermelha

A amostra **x = 8.97** (reta preta) ativa as funções laranja, verde e vermelha, na seguinte ordem de grau de ativação: **vermelha > verde > laranja**. A amostra não ativa a função azul

<br><br><br>

# Questão 3

**Implemente uma função para realizar as seguintes operações fuzzy disponíveis nas
notas de aula: Complemento, Uniao, Interseção e as Normas Duas. Utilize os conjuntos fuzzy propostos nas atividades anteriores para realizar as operações implementadas. Apresente uma analise gráfica e textual comparativa dos resultados obtidos.**

## Implementação

Foram criadas funções para realizar as operações de complemento, união e normas duais. Todas as funções, exceto as duais, recebem um domínio para executar as operações, enquanto as normas duais utilizam os graus de ativação de uma amostra para realizar suas operações.

As funções implementadas incluem:

- **Complemento**: recebe um domínio e retorna os complementos de cada função do domínio em um vetor.
- **União**: recebe um domínio e retorna um conjunto fuzzy que representa a união de todas as funções do domínio, utilizando a regra do maior grau dentre as funções.
- **Interseção**: recebe um domínio e retorna um conjunto fuzzy que representa a interseção de todas as funções do domínio, aplicando a regra do menor grau dentre as funções.
- **TNorma**: recebe os graus de ativação, o tipo de T-norma e um valor (usado em algumas T-normas), e retorna o resultado da operação conforme o tipo de T-norma.
- **SNorma**: recebe os graus de ativação, o tipo de S-norma e um valor (usado em algumas S-normas), e retorna o resultado da operação conforme o tipo de S-norma.

As regras de T-norma implementadas são válidas para n valores, sendo apresentadas abaixo apenas para dois valores:

|            Tipo            |                 Retorno                |
|:--------------------------:|:--------------------------------------:|
|        **Min Zadeh**       |                min(a, b)               |
|   **Produto Algébrico**    |                   a.b                  |
| **Lukasiewicz p ≥ 1**      |       max[0, (1+p)(a+b-1)-p.a.b]       |
| **Hamacher γ > 0**         | (a.b)/(γ+(1-γ)(a+b-a.b))               |
|   **Diferença Limitada**   |              max(a+b-1, 0)             |
|  **Weber Prod. Drástico**  | a se b=1; b se a=1; 0 caso contrário    |

As regras de S-norma implementadas também são válidas para n valores, sendo apresentadas abaixo apenas para dois valores:

|            Tipo            |                     Retorno                   |
|:--------------------------:|:---------------------------------------------:|
|        **Max Zadeh**       |                    max(a, b)                  |
|  **Soma Probabilística**   |                     a+b-a.b                   |
| **Lukasiewicz p ≥ 0**      |             min[1, (a+b-1+p.a.b)]             |
| **Hamacher γ > 0**         | (a+b-a.b-(1-γ)a.b)/(1-(1-γ)a.b)             |
|      **Soma Limitada**     |                   min(a+b, 1)                 |
|  **Weber Soma Drástico**   |     a se b=0; b se a=0; 1 caso contrário      |

<br>

## Teste

Utilizaram-se os mesmos domínios criados na questão anterior para testar as funções implementadas. A seguir, são apresentados os gráficos gerados. Para cada domínio foi feito os complementos, a união, a s-norma Soma Probabilística, a interseção e t-norma Produto Algébrico das funções dos domínios.

Em todos os gráficos no canto superior esquerdo mostra o subgráfico do domínio original, com limites de 0 a 10. Logo abaixo, no canto inferior esquerdo, está os **complementos** das funções do domínio original.

Além disso em todos os gráficos na parte superior central está um subgráfico com o resultado da **União** das funções do domínio original, em que o valor de uma amostra é determinado pelo maior grau de ativação entre as funções. Abaixo, no subgráfico inferior central, temos o resultado da **S-norma Soma Probabilística** das funções do domínio, em que o valor de uma amostra é dado pela soma dos graus de ativação menos o produto desses graus para as funções do domínio.

Da mesma forma em todos os gráficos no canto superior direito está o subgráfico que representa a **Interseção** das funções do domínio original, em que o valor de uma amostra é o menor grau de ativação entre as funções. Finalmente, no canto inferior direito, o subgráfico exibe o resultado da **T-norma Produto Algébrico** das funções do domínio original, onde o valor de uma amostra corresponde ao produto dos graus de ativação das funções.

### Domínio Triangular

<img src="data/imgs/operations/Triangular.png">

Observa-se que o gráfico da T-norma possui uma forma semelhante ao da Interseção, com a principal diferença na escala dos valores: os valores da T-norma são menores que os da Interseção.

### Domínio Trapezoidal

<img src="data/imgs/operations/Trapezoidal.png">

Assim como no domínio triangular, o gráfico da T-norma é semelhante ao da Interseção, com os valores da T-norma apresentando uma escala menor.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Domínio Gaussiana

<img src="data/imgs/operations/Gaussiana.png">

O gráfico da S-norma exibe características similares ao da União. Em regiões de subidas e descidas acentuadas na União, observa-se um comportamento semelhante na S-norma. Além disso, a T-norma apresenta forma parecida à Interseção, mas com uma escala de valores bem menor.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Domínio Sigmoidal

<img src="data/imgs/operations/Sigmoidal.png">

O gráfico da S-norma adota uma estrutura em "escada" semelhante à União. Em vez de estabilizar no primeiro patamar, a S-norma eleva o nível de ativação sempre que uma nova função começa a influenciar a amostra. Já a T-norma é visualmente idêntica à Interseção, com forma e escala praticamente idênticas.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Domínio Sino

<img src="data/imgs/operations/Sino.png">

O gráfico da S-norma é similar ao da União, embora apresente vales mais rasos e picos centrais ligeiramente mais elevados. A T-norma, por sua vez, possui uma forma análoga à Interseção, mas com uma escala de valores consideravelmente menor.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Domínio S

<img src="data/imgs/operations/S-shaped.png">

No gráfico da S-norma, observa-se a estrutura de "escada" semelhante à União, onde o nível de ativação se eleva gradualmente conforme cada nova função influencia a amostra. A T-norma, por outro lado, mantém uma aparência visual idêntica à Interseção, tanto em forma quanto em escala.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Domínio Z

<img src="data/imgs/operations/Z-shaped.png">

A S-norma exibe uma estrutura de "escada" similar à União, mas, diferentemente da União, ela diminui o nível de ativação conforme cada função deixa de influenciar a amostra. A T-norma é visualmente idêntica à Interseção em forma e escala.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Domínio Cauchy

<img src="data/imgs/operations/Cauchy.png">

O gráfico da S-norma é parecido com o da União, porém apresenta picos e vales centrais mais elevados. A T-norma, por outro lado, tem uma forma semelhante à Interseção, mas com valores em uma escala menor.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Domínio Gaussiana Dupla

<img src="data/imgs/operations/Gaussiana Dupla.png">

A T-norma exibe uma forma próxima à da Interseção, diferenciando-se apenas na escala de valores, que é menor na T-norma.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Domínio Retangular

<img src="data/imgs/operations/Retangular.png">

No domínio retangular, tanto a União e a S-norma quanto a Interseção e a T-norma apresentam gráficos idênticos, sem distinções visuais entre essas operações.

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Domínio Laplace

<img src="data/imgs/operations/Laplace.png">

O gráfico da S-norma é visualmente semelhante ao da União, com a diferença de que os vales da União são mais afunilados. A T-norma possui uma forma semelhante à Interseção, mas com duas diferenças: enquanto a Interseção tem um único valor máximo, a T-norma mantém um intervalo máximo, além de apresentar uma escala de valores consideravelmente menores.

# Questão 4

**Implemente uma função para calcular uma relação fuzzy. A função deve receber como entrada a t-norma (ja implementadas anteiormente), o tamanho dos dois conjuntos fuzzy, os graus de pertinencia de cada elemento do conjunto. A função deve retornar o resultado da relação. Cuidado com as exceções e operações indevidas. Apresente um exemplo de execução comparando o resultado utilizando ao menos dois operadores para t-norma e dois para s-norma. presente uma analise gráfica e textual comparativa dos resultados obtidos.**

## Implementação

## Teste

# Questão 5

**Implemente uma func¸ao para calcular as composições Max-Min, Min-Max e Max-Prod. Cuidado com as exceções e operações indevidas. Execute o mesmo exemplo para as tres composições. Apresente uma análise gráfica e textual comparativa dos resultados obtidos.**

</div>