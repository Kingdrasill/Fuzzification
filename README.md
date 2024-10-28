<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" }); </script>

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

### Triangular - TR

A função recebe os valores ***a***, ***b*** e ***c*** que definem a forma do triângulo. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \left\{\begin{matrix}
                    0 & x \leq a \\
                    \frac{x-a}{b-a} & a < x \leq b \\
                    \frac{c-x}{c-b} &  b < x \leq c \\
                    0 & x > c  \\
                    \end{matrix}\right.
$$

### Trapezoidal - TP

A função recebe os valores ***a***, ***b***, ***c*** e ***d*** que definem a forma do trapézio. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \left\{\begin{matrix}
                    0 & x \leq a \\
                    \frac{x-a}{b-a} & a < x \leq b \\
                    1 &  b < x \leq c \\
                    \frac{d-x}{d-c} &  c < x \leq d \\
                    0 & x > d  \\
                    \end{matrix}\right.
$$

### Gaussiana - GS

A função recebe os valores ***c*** que é o centro da curva e ***$\sigma$*** que é o desvio padrão que controla a largura. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = exp\left(\frac{-(x-c)^2}{2\sigma^2}\right)
$$

### Sigmoidal - SG

A função recebe os valores ***a*** que controla a inclinação e ***c*** que é a posição central. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \frac{1}{1 + exp\left(-a(x-c)\right)}
$$

### Sino - SN

A função recebe os valores ***a*** que controla a largura, ***b*** que controla a suavidade e ***c*** que é o ponto central. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \frac{1}{1 + \left|\frac{x-c}{a}\right|^{2b}}
$$

### S-shaped - SS

A função recebe os valores ***a*** e ***b*** que são os pontos de controle da função. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \left\{\begin{matrix}
                    1 & x \leq a \\
                    2\left(\frac{x-b}{b-a}\right)^2 & a < x \leq \frac{a+b}{2} \\
                    1 - 2\left(\frac{b-x}{b-a}\right)^2 &  \frac{a+b}{2} < x \leq b \\
                    0 & x > b  \\
                    \end{matrix}\right.
$$

### Z-shaped - ZS

A função recebe os valores ***a*** e ***b*** que são os pontos de controle da função. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \left\{\begin{matrix}
                    1 & x \leq a \\
                    1 - 2\left(\frac{x-b}{b-a}\right)^2 & a < x \leq \frac{a+b}{2} \\
                    2\left(\frac{b-x}{b-a}\right)^2 &  \frac{a+b}{2} < x \leq b \\
                    0 & x > b  \\
                    \end{matrix}\right.
$$

### Cauchy - CC

A função recebe os valores ***x_0*** é o parâmetro de localização que especifica a localização do pico da distribuição e ***$\gamma$*** é o parâmetro de escala que especifica a meia largura no meio máximo. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \frac{1}{\pi\gamma\left[1+\left(\frac{x-x_0}{\gamma}\right)^2\right]}
$$

### Gaussiana Dupla - GD

A função recebe os valores ***$\mu$*** que é a localização do centro, ***$\sigma_1$*** que controla a distribuição no lado esquerdo e ***$\sigma_2$*** que controla a distribuição no lado direito. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \left\{\begin{matrix}
                    Aexp\left(-\frac{\left(x-\mu\right)^2}{2\sigma_1^2}\right) & x < \mu \\
                    Aexp\left(-\frac{\left(x-\mu\right)^2}{2\sigma_2^2}\right) & \text{caso contrário} \\
                    \end{matrix}\right.
$$

$$
\text{Em que } A = \sqrt{2/\pi}\left(\sigma_1+\sigma_2\right)^{-1}
$$

### Retangular - RT

A função recebe os valores ***a*** que é o limite inferior do intervalo onde a pertinência é 1 e ***b*** que é o limite superior do intervalo onde a pertinência é 1. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \left\{\begin{matrix}
                    1 & a \leq x \leq b \\
                    0 & \text{caso contrário} \\
                    \end{matrix}\right.
$$

### Laplace - LP

A função recebe os valores ***$\mu$*** que é o parâmetro de localização do centro e ***b*** que é o parâmetro de escala. 

O valor de x passado para a função é calculado pela seguinte formúla:

$$
\mu_A(x) = \frac{1}{2b}exp\left(-\frac{\left|x-\mu\right|}{b}\right)
$$

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