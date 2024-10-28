<div style="display: none;">
  <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" }); </script>
</div>

# Fuzzification

## Gabriel Teixeira Júlio

## Questão 1

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

Todas as funções implementadas recebem como parâmetros as seguintes informações:

- **inf** - Limite inferior da função
- **sup** - Limite superior da função
- ***Contantes*** - Valores que dependem do tipo da função, que são usados para formar a função
- **x** - Valor a ser calculado o grau de pertinência

### Função Triangular

A função recebe os valores ***a***, ***b*** e ***c*** que definem a forma do triângulo. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/1.jpg)

### Função Trapezoidal

A função recebe os valores ***a***, ***b***, ***c*** e ***d*** que definem a forma do trapézio. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/2.jpg)

### Função Gaussiana

A função recebe os valores ***c*** que é o centro da curva e ***$\sigma$*** que é o desvio padrão que controla a largura. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/3.jpg)

### Função Sigmoidal

A função recebe os valores ***a*** que controla a inclinação e ***c*** que é a posição central. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/4.jpg)

### Função Sino

A função recebe os valores ***a*** que controla a largura, ***b*** que controla a suavidade e ***c*** que é o ponto central. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/5.jpg)

### Função S

A função recebe os valores ***a*** e ***b*** que são os pontos de controle da função. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/6.jpg)

### Função Z

A função recebe os valores ***a*** e ***b*** que são os pontos de controle da função. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/7.jpg)

### Função Cauchy

A função recebe os valores ***x_0*** é o parâmetro de localização que especifica a localização do pico da distribuição e ***$\gamma$*** é o parâmetro de escala que especifica a meia largura no meio máximo. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/8.jpg)

### Função Gaussiana Dupla

A função recebe os valores ***$\mu$*** que é a localização do centro, ***$\sigma_1$*** que controla a distribuição no lado esquerdo e ***$\sigma_2$*** que controla a distribuição no lado direito. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/9.jpg)

### Função Retangular

A função recebe os valores ***a*** que é o limite inferior do intervalo onde a pertinência é 1 e ***b*** que é o limite superior do intervalo onde a pertinência é 1. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/10.jpg)

### Função Laplace

A função recebe os valores ***$\mu$*** que é o parâmetro de localização do centro e ***b*** que é o parâmetro de escala. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/11.jpg)

### Exemplo

Para poder testar se as funções estão funcionado corretamente foi criado um metódo que lê de um arquivo *txt* as funções a serem testadas e seus parâmetros, depois é calculado o grau de pertinência de um valor passado pelo usuário.

A seguir está o grau de pertinência para **x = 6** para todas as funções implementadas:

- **Triangular** [a=3, b=6, c=8]: 
  - O grau de pertinência de x = 6 é  **1.0** 
- **Trapezoidal** [a=1, b=5, c=7, d=8]: 
  - O grau de pertinência de x = 6 é **1.0**
- **Gaussiana** [c=5, $\sigma$=2]: 
  - O grau de pertinência de x = 6 é **0.8824969025845955**
- **Sigmoidal** [a=2, c=4]: 
  - O grau de pertinência de x = 6 é **0.9820137900379085**
- **Sino** [a=2, b=4, c=6]: 
  - O grau de pertinência de x = 6 é **1.0**
- **S-shaped** [a=1, b=8]: 
  - O grau de pertinência de x = 6 é **0.8367346938775511**
- **Z-shaped** [a=3, b=7]: 
  - O grau de pertinência de x = 6 é **0.125**
- **Cauchy** [$x_0$=6, $\gamma$=2]: 
  - O grau de pertinência de x = 6 é **0.15915494309189535**
- **Gaussiana Dupla** [$\mu$=7, $\sigma_1$=3, $\sigma_2$=1]: 
  - O grau de pertinência de x = 6 é **0.18869161384649658**
- **Retangular** [a=2, b=6]: 
  - O grau de pertinência de x = 6 é **1.0**
- **Laplace** [$\mu$=4, b=3]: 
  - O grau de pertinência de x = 6 é **0.08556951983876533**

## Questão 2

**Defina o domínio (universo de discurso) para uma variável de entrada a sua escolha. Particione esse universo de discurso em no mínimo 4 funções de pertinência uniformemente espac¸adas. Realize a fuzzificac¸ao (calculo do grau de ativação das funções) para duas amostras considerando cada uma das funções apresentadas na atividade anterior. Apresente uma análise gráfica e textual comparativa dos resultados obtidos.**

Foi criada uma classe para representaar o domínio de uma variável de entrada Fuzzy. A classe armazena os seguintes dados:

- **inf** - qual o limite inferior do domínio
- **sup** - qual o limite superior do domínio
- **fncs** - quais as funções estão no domíno

A variável ***fncs*** é um dicionário que armazena as seguintesinformações das funções do domíno:

- **values** - um vetor que guarda os valores das contantes para usar nas funções de calcular pertinência de valor nas funções do domínio
- **func** - que armazena a função que deve ser chamada na hora dq calcular a pertinência de um valor nas funções do domínio
- **name** - o nome das funções que estão no domínio

A classe também possui dois metódos:

- **calcularGrauAtivacao** - que recebe um valor x e calcula o grau de ativação de x nas funções no domínio 
- **plotarGrauAtivacao** - que recebe dois valores x1 e x2, e o diretório onde o gráico gerado será armazenado. Está função plota um gráfico com todas as funções no domínio e linhas verticais mostrando onde elas são cortadas nos valores x1 e x2

### Exemplo

Foi sorteado um número entre 4 e 6 que define o número de funções dentro do domínio, depois o usuário passa os valores das duas amostras e com isso começa a fuzzificação para todos os tipos de funçõe implementadas. As funções do domínio são uniforma espaçadas porém são aletórias, ou seja, todos os valores menos os valores de posição são gerados aleatoriamente. Após achar o grau de ativação das amostras nas funções do domínio é plotado um gráfico que mostra onde as amostras cortam as funções do domínio, sendo este gráfico salvo num arquivo.

A seguir estão os gráficos e os graus de ativação para as amostras **x=2** e **x=5**:

#### Função Triangular

<img src="data/imgs/domains/Triangular.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0.05213270142180089
  - **x=5**: 0
- $\mu_{f2}$
  - **x=2**: 0.9533364442370509
  - **x=5**: 0.5333644423705087
- $\mu_{f3}$
  - **x=2**: 0.6268656716417911
  - **x=5**: 0.7791519434628976
- $\mu_{f4}$
  - **x=2**: 0.3421052631578948
  - **x=5**: 1.0
- $\mu_{f5}$
  - **x=2**: 0.4646271510516252
  - **x=5**: 0.8087954110898661
- $\mu_{f6}$
  - **x=2**: 0
  - **x=5**: 0

A amostra x=2 tem o maior grau de ativação na função laranja e o menor grau na função marrom. Já a amostra x=5 tem o maior grau de ativação na função vermelha e o menor grau nas funções azul e marrom.

#### Função Trapezoidal

<img src="data/imgs/domains/Trapezoidal.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0.948555260224642
  - **x=5**: 0.6141644516848153
- $\mu_{f2}$
  - **x=2**: 0.9064108563406644
  - **x=5**: 0.28591830905455573
- $\mu_{f3}$
  - **x=2**: 0.5414596866641193
  - **x=5**: 0.9294880834861092
- $\mu_{f4}$
  - **x=2**: 0.5275928709469615
  - **x=5**: 0.9463173716985183
- $\mu_{f5}$
  - **x=2**: 0
  - **x=5**: 0
- $\mu_{f6}$
  - **x=2**: 0
  - **x=5**: 0

A amostra x=2 tem o maior grau de ativação na função azul. Já a amostra x=5 tem o maior grau de ativação na função vermelha. Ambas as amostras tem o menor grau de ativação nas funções lilás e marrom.

#### Função Gaussiana

<img src="data/imgs/domains/Gaussiana.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0.9677020823205547
  - **x=5**: 0.2773538521413458
- $\mu_{f2}$
  - **x=2**: 0.8334516418132575
  - **x=5**: 0.3202598827031787
- $\mu_{f3}$
  - **x=2**: 0.0008935783547046066
  - **x=5**: 0.5038010251735885
- $\mu_{f4}$
  - **x=2**: 2.390063497768091e-06
  - **x=5**: 0.6195850652630459
- $\mu_{f5}$
  - **x=2**: 3.6737448583504213e-16
  - **x=5**: 0.0020908911388562482
- $\mu_{f6}$
  - **x=2**: 0.012511528656489343
  - **x=5**: 0.2741606941973955

A amostra x=2 tem o maior grau de ativação na função azul e o menor grau na função lilás. Já a amostra x=5 tem o maior grau de ativação na função vermelha e o menor grau na função lilás.

#### Função Sigmoidal

<img src="data/imgs/domains/Sigmoidal.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0.9994472213630764
  - **x=5**: 0.9999999928058669
- $\mu_{f2}$
  - **x=2**: 0.5
  - **x=5**: 0.9899491861165264
- $\mu_{f3}$
  - **x=2**: 0.0011349852430780928
  - **x=5**: 0.9673905446932344
- $\mu_{f4}$
  - **x=2**: 0.0009110511944006454
  - **x=5**: 0.14804719803168948
- $\mu_{f5}$
  - **x=2**: 3.0374584085834906e-12
  - **x=5**: 1.742827536238062e-06
- $\mu_{f6}$
  - **x=2**: 0.16798161486607552
  - **x=5**: 0.2689414213699951

A amostra x=2 tem o maior grau de ativação na função azul e o menor grau na função lilás. Já a amostra x=5 tem o maior grau de ativação na função azul e o menor grau na função lilás. 

A mostra x=2 está na zona de maximização apenas da função azul. Já a amostra x=5 está na zona de maximização das funções azul, laranja e verde.

#### Função Sino

<img src="data/imgs/domains/Sino.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0.7867474741857144
  - **x=5**: 0.03377668931483294
- $\mu_{f2}$
  - **x=2**: 0.9879496789780278
  - **x=5**: 0.18482365712887466
- $\mu_{f3}$
  - **x=2**: 0.27682750128961875
  - **x=5**: 0.9266897695979149
- $\mu_{f4}$
  - **x=2**: 0.04528455144022548
  - **x=5**: 0.9266897695979149
- $\mu_{f5}$
  - **x=2**: 0.01249619398014668
  - **x=5**: 0.18482365712887475
- $\mu_{f6}$
  - **x=2**: 0.004779963316138125
  - **x=5**: 0.03377668931483286

A amostra x=2 tem o maior grau de ativação na função laranja e o menor grau na função marrom. Já a amostra x=5 tem o maior grau de ativação nas funções verde e vermelha e o menor grau nas funções azul e marrom. 

Pelo modo que as funções sino foram geradas a amostra x=5 ficou no centro do domínio logo seus valores nas três funções a esquerda dela é espelhado nos seus valores nas três funções a direita dela. 

#### Função S

<img src="data/imgs/domains/S-shaped.png" height="300">

- $\mu_{f1}$
  - **x=2**: 1
  - **x=5**: 1
- $\mu_{f2}$
  - **x=2**: 0
  - **x=5**: 1
- $\mu_{f3}$
  - **x=2**: 0
  - **x=5**: 1
- $\mu_{f4}$
  - **x=2**: 0
  - **x=5**: 0
- $\mu_{f5}$
  - **x=2**: 0
  - **x=5**: 0
- $\mu_{f6}$
  - **x=2**: 0
  - **x=5**: 0

A amostra x=2 tem o maior grau de ativação na função azul e o menor grau nas funções laranja, verde, vermelha, lilás e marrom. Já a amostra x=5 tem o maior grau de ativação nas funções azul, laranja e verde, e o menor grau nas funções lilás e marrom. 

#### Função Z

<img src="data/imgs/domains/Z-shaped.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0
  - **x=5**: 0
- $\mu_{f2}$
  - **x=2**: 0.92
  - **x=5**: 0
- $\mu_{f3}$
  - **x=2**: 1
  - **x=5**: 0
- $\mu_{f4}$
  - **x=2**: 1
  - **x=5**: 1
- $\mu_{f5}$
  - **x=2**: 1
  - **x=5**: 1
- $\mu_{f6}$
  - **x=2**: 1
  - **x=5**: 1

A amostra x=2 tem o maior grau de ativação nas funções verde, vermelha, lilás e marrom, e o menor grau na função azul. Já a amostra x=5 tem o maior grau de ativação nas funções vermelha, lilás e marrom, e o menor grau nas funções azul, laranja e verde. 

A função z e s são quase perfeitamente inversa, não sendo totalmente inversa quando uma das funções tem um limite no limite do domínio.

#### Função Cauchy

<img src="data/imgs/domains/Cauchy.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0.07530035852418082
  - **x=5**: 0.016830645971803213
- $\mu_{f2}$
  - **x=2**: 0.43731999688215734
  - **x=5**: 0.014276231473278032
- $\mu_{f3}$
  - **x=2**: 0.054175283200720785
  - **x=5**: 0.03536558207091064
- $\mu_{f4}$
  - **x=2**: 0.026415758189526198
  - **x=5**: 0.3978873577297384
- $\mu_{f5}$
  - **x=2**: 0.02417728536687738 
  - **x=5**: 0.09440231097711296
- $\mu_{f6}$
  - **x=2**: 0.0044870062634567096
  - **x=5**: 0.015865377653269206

A amostra x=2 tem o maior grau de ativação na função laranja e o menor grau na função marrom. Já a amostra x=5 tem o maior grau de ativação na função vermelha e o menor grau na função laranja. 

#### Função Gaussiana Dupla

<img src="data/imgs/domains/Gaussiana Dupla.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0.11868607713846116
  - **x=5**: 0.06034586950817793
- $\mu_{f2}$
  - **x=2**: 0.13144720935796794
  - **x=5**: 0.0947903730032437
- $\mu_{f3}$
  - **x=2**: 1.37846644860361e-27
  - **x=5**: 0.33792307105723485
- $\mu_{f4}$
  - **x=2**: 0.06701362261847961
  - **x=5**: 0.3156022436952836
- $\mu_{f5}$
  - **x=2**: 0.010726185093490588
  - **x=5**: 0.09463924032825762

- $\mu_{f6}$
  - **x=2**: 0
  - **x=5**: 0

A amostra x=2 tem o maior grau de ativação na função laranja e o menor grau na função marrom. Já a amostra x=5 tem o maior grau de ativação na função verde e o menor grau na função marrom. 

#### Função Retangular

<img src="data/imgs/domains/Retangular.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0
  - **x=5**: 0
- $\mu_{f2}$
  - **x=2**: 1
  - **x=5**: 0
- $\mu_{f3}$
  - **x=2**: 0
  - **x=5**: 1
- $\mu_{f4}$
  - **x=2**: 0
  - **x=5**: 1
- $\mu_{f5}$
  - **x=2**: 0
  - **x=5**: 0
- $\mu_{f6}$
  - **x=2**: 0
  - **x=5**: 0

A amostra x=2 tem o maior grau de ativação na função laranja e o menor grau nas funções  azul, verde, vermelha, lilás e marrom. Já a amostra x=5 tem o maior grau de ativação nas funções verde e vermelha, e o menor grau nas funções azul, laranja, lilás e marrom.

A amostra x=5 está no ponto em as funções verde e vermelha se sobrepoem, permitindo ter valor de grau de ativação 1 nas duas.

#### Função Laplace

<img src="data/imgs/domains/Laplace.png" height="300">

- $\mu_{f1}$
  - **x=2**: 0.2007361975433549
  - **x=5**: 0.04908438166244552
- $\mu_{f2}$
  - **x=2**: 0.1170459647621665
  - **x=5**: 0.0767555572178312
- $\mu_{f3}$
  - **x=2**: 0.03019104569937317
  - **x=5**: 0.4504504504504504
- $\mu_{f4}$
  - **x=2**: 0.113
  - **x=5**: 0.4504504504504504
- $\mu_{f5}$
  - **x=2**: 2.9528190431964766e-05
  - **x=5**: 0.003729595614158312
- $\mu_{f6}$
  - **x=2**: 0.003839058048144878
  - **x=5**: 0.018775045551918897
  
A amostra x=2 tem o maior grau de ativação na função azul e o menor grau na função  lilás. Já a amostra x=5 tem o maior grau de ativação na função verde e o menor grau na função lilás.

## Questão 3

**Implemente uma função para realizar as seguintes operações fuzzy disponíveis nas
notas de aula: Complemento, Uniao, Interseção e as Normas Duas. Utilize os conjuntos fuzzy propostos nas atividades anteriores para realizar as operações implementadas. Apresente uma analise gráfica e textual comparativa dos resultados obtidos.**

Foi criado funções para fazer as operções de complemento, união e noramas duais. Todas as funções menos as duais recebem um domínio para fazer as operções em cima, já as normas duais recebem os graus de ativação de uma amostra para fazer uma operação por cima.

As funções criadas foram:

- ***Complemento*** - recebe um domíno e retorna os complementos de cada função do domíno num vetor 
- ***União*** - recebe um domínio e retorna um conjunto fuzzy com a união de todos as funções do domínio, sendo a regra o maior grau dentre as funções
- ***Interseção***- recebe um domínio e retorna um conjunto fuzzy com a interseção de todos as funções do domínio, sendo a regra o menor grau dentre as funções
- ***TNorma*** - recebe os graus de ativação, o tipo de T-norma e um valor que é usado em algumas T-normas e retorna o valor da regra pelo tipo de T-norma
- ***SNorma*** - recebe os graus de ativação, o tipo de S-norma e um valor que é usado em algumas S-normas e retorna o valor da regra pelo tipo de S-norma

As regras T-norma implementadas são para n valores, abaixo estão elas apenas para dois valores:

- **Min Zadeh** - retorna min(a, b)
- **Produto Algébrico** - retorna a.b
- **Lukasiewicz p $\geq$ 1** - retorna max[0, (1+p)(a+b-1)-p.a.b]
- **Hamacher $\gamma >$ 0** - retorna (a.b)/($\gamma$+(1-$\gamma$)(a+b-a.b))
- **Diferença Limitada** - retorna max(a+b-1, 0)
- **Weber Prod. Drástico** - retorna a se b=1; b se a = 1; 0 caso contrário

As regras S-norma implementadas são para n valores, abaixo estão elas apenas para dois valores:

- **Max Zadeh** - retorna max(a,b)
- **Soma Probabilística** - retorna a+b-a.b
- **Lukasiewicz p $\geq$ 0** - retorna min[1, (a+b-1+p.a.b)]
- **Hamacher $\gamma >$ 0** - retorna (a+b-a.b-(1-$\gamma$)a.b)/(1-(1-$\gamma$)a.b)
- **Soma Limitada** - retorna min(a+b, 1)
- **Weber Soma Drástico** - retorna a se b=0; b se a = 0; 1 caso contrário

### Exemplo

Foi utilizado os mesmos domínios criados para questão anterior para testar as funções implementadas, a seguir estão os gráficos gerados.

#### Função Triangular

<img src="data/imgs/operations/Triangular.png" height="500">

#### Função Trapezoidal

<img src="data/imgs/operations/Trapezoidal.png" height="500">

#### Função Gaussiana

<img src="data/imgs/operations/Gaussiana.png" height="500">

#### Função Sigmoidal

<img src="data/imgs/operations/Sigmoidal.png" height="500">

#### Função Sino

<img src="data/imgs/operations/Sino.png" height="500">

#### Função S

<img src="data/imgs/operations/S-shaped.png" height="500">

#### Função Z

<img src="data/imgs/operations/Z-shaped.png" height="500">

#### Função Cauchy

<img src="data/imgs/operations/Cauchy.png" height="500">

#### Função Gaussiana Dupla

<img src="data/imgs/operations/Gaussiana Dupla.png" height="500">

#### Função Retangular

<img src="data/imgs/operations/Retangular.png" height="500">

#### Função Laplace

<img src="data/imgs/operations/Laplace.png" height="500">

Todos as operações foram geradas corretamente. A S-Norma Soma Probabilística e T-Norma Produto Algébrico foram escolhidas como a s-norma e t-norma a serem plotadas pois seus gráficos parecem muito com a união e interseção respectivamente porém não exatamente igual e tenha escalas diferentes da para perceber um nível de semelhança.

## Questão 4

**Implemente uma função para calcular uma relaçõo fuzzy. A função deve receber como entrada a t-norma (ja implementadas anteiormente), o tamanho dos dois conjuntos fuzzy, os graus de pertinencia de cada elemento do conjunto. A função deve retornar o resultado da relação. Cuidado com as exceções e operações indevidas. Apresente um exemplo de execução comparando o resultado utilizando ao menos dois operadores para t-norma e dois para s-norma. presente uma analise gráfica e textual comparativa dos resultados obtidos.**

## Questão 5

**Implemente uma func¸ao para calcular as composições Max-Min, Min-Max e Max-Prod. Cuidado com as exceções e operações indevidas. Execute o mesmo exemplo para as tres composições. Apresente uma análise gráfica e textual comparativa dos resultados obtidos.**