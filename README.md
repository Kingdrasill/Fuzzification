<div style="display: none;">
  <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" }); </script>
</div>

# Fuzzification

## Gabriel Teixeira Júlio

O objetivo deste projeto foi o iniciar a implementação na mão de um sistema Fuzzy no ***Python***. Este projeto trata da parte de fuzzicação englobando os seguintes tópoicos:

- Funções de Pertinência
- Conjuntos Fuzzy
- Operações de Conjuntos Fuzzy
- Relações de Conjuntos Fuzzy
- Composição de Conjuntos Fuzzy

## Funções de Pertinência

No arquivo ***functions.py*** está a implementação de funções que retornam o grau de pertinência de um determindo valor em uma função dentre as que vão ser detalhadas a seguir.

Todas as funções recebem como parâmetros as seguintes informações:

- **inf** - Limite inferior da função
- **sup** - Limite superior da função
- ***Contantes*** - Valores que dependem do tipo da função, que são usados para formar a função
- **x** - Valor a ser calculado o grau de pertinência

### Triangular

A função recebe os valores ***a***, ***b*** e ***c*** que definem a forma do triângulo. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/1.jpg)

### Trapezoidal
A função recebe os valores ***a***, ***b***, ***c*** e ***d*** que definem a forma do trapézio. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/2.jpg)

### Gaussiana

A função recebe os valores ***c*** que é o centro da curva e ***$\sigma$*** que é o desvio padrão que controla a largura. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/3.jpg)

### Sigmoidal

A função recebe os valores ***a*** que controla a inclinação e ***c*** que é a posição central. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/4.jpg)

### Sino

A função recebe os valores ***a*** que controla a largura, ***b*** que controla a suavidade e ***c*** que é o ponto central. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/5.jpg)

### S-shaped

A função recebe os valores ***a*** e ***b*** que são os pontos de controle da função. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/6.jpg)

### Z-shaped

A função recebe os valores ***a*** e ***b*** que são os pontos de controle da função. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/7.jpg)

### Cauchy

A função recebe os valores ***x_0*** é o parâmetro de localização que especifica a localização do pico da distribuição e ***$\gamma$*** é o parâmetro de escala que especifica a meia largura no meio máximo. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/8.jpg)

### Gaussiana Dupla

A função recebe os valores ***$\mu$*** que é a localização do centro, ***$\sigma_1$*** que controla a distribuição no lado esquerdo e ***$\sigma_2$*** que controla a distribuição no lado direito. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/9.jpg)

### Retangular

A função recebe os valores ***a*** que é o limite inferior do intervalo onde a pertinência é 1 e ***b*** que é o limite superior do intervalo onde a pertinência é 1. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/10.jpg)

### Laplace

A função recebe os valores ***$\mu$*** que é o parâmetro de localização do centro e ***b*** que é o parâmetro de escala. 

O valor de x passado para a função é calculado pela seguinte formúla:

![alt text](data/equations/11.jpg)

### Exemplo

Para poder testar se as funções estão funcionado corretamente foi criado um metódo que lê de um arquivo *txt* as funções a ser testadas e seus parâmetros, depois é calculado o grau de pertinência de um valor passado pelo usuário.

A seguir estão os parâmetros das funções e o grau de pertinência para **x = 6**:

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