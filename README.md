# Jogo_Multiplos

Jogo aonde voce precisa descobrir se o numero é multiplos ou não do numero correspondente.

# Executar o projeto

# Executar o projeto linux
Instalar o pyhton na máquina linux - versão 3
```sudo python3 get-pip.py```

Instalar o pygame:
```pip install pygame```

Executar o projeto:
```python3 index.py```

# Executar o projeto no Window

Comandos serão executados dentro do projeto

Instalar o pygame:
```py -m pip install -U pygame```

Executar o jogo:
```py index.py```

# Como funciona

Para que fosse feito esse jogo, foi utilizado a bliblioteca pygame. Para instalar no seu projeto é preciso executar esse comando 'python -m pip install -U pygame' .
Dúvidas entre no site https://www.pygame.org/wiki/GettingStarted.

# Objetivo

O objetivo do Jogo é somar os numeros, e com o resultado descobri se o numero é multiplo de 5. Se for multiplo de 5 irá sumir da tela e terá uma pontuação.

Teremos 3 colunas verticais:

| Coluna 1 | Coluna 2 | Coluna 3 |
| --- | ---- | ----|
| 3   |  4   |  1  |
|2    |  2   |    5|
|1    | 2    |    7|

Uma linha horizontal:
| Linha horizontal  |
| ---      |
|2   4  5  |

O usuário irá selecionar no máximo 3 números, a soma deles precisa dar um multiplo de 5.

| Coluna 1 | Coluna 2 | Coluna 3 |
| --- | ---- | ----|
| (3)   |  4   |  1  |
|2    |  2   |    5|
|1    | 2    |    7|

| Linha horizontal  |
| ---               |
|(2)   4  5 3 7       |

O número 3 irá sumir, e o número 2 irá ter outro número

# Pontuação

A pontuação será calculada da seguinte forma:

| Valor | Pontuação |
| ---   | ----      |
| 5     |  1        |
| 10    |  2        |

Será de acordo com a tábuada, qual o valor que irá calcular, que terá o valor igual a 5 na tábuada de 5, é o 1, essa será a pontução.