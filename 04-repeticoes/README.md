# Computational Thinking Using PYTHON

Aqui terá os exercícios propostos durante as aulas de Python.

Resoluções do professor: https://github.com/egondo/1tdsr

## Problemas

**4.1** Dados uma sequência de 5 números inteiros. Calcule a soma de todos os números da sequência. <br>
    Resolva usando apenas duas variáveis:

<br>

**4.2** Dado um número inteiro positivo *n*, escreva um algoritmo que imprime a tabuada de *n* até o valor 10. <br>

<br>

**4.3** Escreva um algoritmo que dados um número interio porsitivo *n*, imprime na tela todos os númeors de 1 a *n*.

<br>

**4.4** Escreva um programa que dadas duas notas de 0 a 10 calcula a média aritmética entre elas. <br>
    *OBS: Criar um validador que não permite notas fora do intervalo*

<br>

**4.5** Escreva um programa que dado um inteiro *n* positivo, calcula e imprime a soma de todos os números <br>
    interiros entre 1 e *n*.

<br>

**4.6** Escreva um algoritmo que recebe um inteiro prositivo *num* e imprime todo os divisores positivos de *num*. <br>
    *Exemplo: Suponha que $num = 28$, nessa situação devemos imprimir os números 1, 2, 4, 7, e 28, que todos os* <br>
    *divisores do 28.*

<br>

---

## Lista de Exercício 3

1.  Dada uma sequência de números inteiros onde o último elemento é o $0$, escreva um algoritmo que calcula a soma <br>
    dos números pares da sequência.

<br>

2.  Dados o número $n$ de alunos de uma turma de Algoritmos e suas notas da primeira prova, determinar a média das <br>
    notas dessa turma. Considere que o usuário digite as informações corretamente.

<br>

3.  Altere o algoritmo anterior para, além da média, contar os alunos que tiraram entre 0 e 5, 0 $(0 ≤ nota < 5, 0)$ <br>
    e acima de 5, 0 $(nota ≥ 5, 0)$.

<br>

4.  Dados $n$ um inteiro positivo e uma sequência de $n$ números reais, escreva um algoritmo que conta e imprime a <br>
    quantidade de números positivos e a quantidade de números negativos.

<br>

5.  Escreva um algoritmo que, dados um número inteiro positivo $n$, imprime na tela a contagem de todos os divisores <br>
    positivos de $n$.

<br>

6.  Em uma prova de concurso com 70 questões haviam 20 pessoas concorrendo. Sabendo que cada questão vale 1 ponto, <br>
    escreva um algoritmo que lê a pontuação da prova obtida de cada um dos candidatos e calcula: <br>
    
    a)  a maior e a menor nota <br>
    b)  o percentual de candidatos que acertaram até 20 questões, o percentual que acertaram de 21 a 50 e o <br>
        percentual que acertou acima de 50 questões

<br>

7.  A conversão de graus Fahrenheit para centígrados é obtida pela fórmula $C = 5/9 \; .\;(F − 32)$. Escreva um algoritmo <br>
    que calcule e escreva uma tabela de graus centígrados em função de graus Fahrenheit que variem de 50 a 150 <br>
    Fahrenheit de 1 em 1.

<br>

8.  Um número inteiro positivo $n$ é denominado **primo** se existirem apenas dois divisores inteiros positivos dele: <br>
    o 1 e o próprio $n$. Escreva um algoritmo que recebe um inteiro $n$ e verifica se $n$ é primo ou não.

<br>

9.  Dados um montante em dinheiro inicial $d$, uma taxa de juros mensal $j$ e um período de tempo em meses $t$, <br>
    escreva um algoritmo que calcula o valor final em dinheiro se $d$ ficar aplicado a taxa de juros $j$ durante <br>
    $t$ meses.

<br>

10. Escreva um algoritmo que recebe um inteiro positivo $n$ e calcula $n! = 1\; ·\;2 \;· \; 3 \; · \; ... \; · \;(n − 1)\;·\; n$. <br>
    Por exemplo, se $n = 6$, então $6! = 1\; ·\; 2\; ·\; 3\; ·\; 4\; ·\; 5\; ·\; 6 = 720$.

<br>

11. Se $Fn$ é o $n-ésimo$ número da sequência de Fibonacci, podemos calculá-la através da seguinte fórmula de recorrência:

    $F_n\; =\; 1\quad\quad\quad\quad\quad\quad se\; n = 1\quad ou\quad n = 2$ <br>
    $F_n\; = F_{n-1}\; +\; F_{n-2}\quad se\; n > 2$

    Vamos mostrar os 10 primeiros números da sequência de Fibonacci:

    $\quad1,\; 1,\; 2,\; 3,\; 5,\; 8,\; 13,\; 21,\; 34,\; 55$

    Escreva um algoritmo que dado $n$, calcula o $n-ésimo$ número da sequência de Fibonacci.

12. Dizemos que um número natural n é palíndromo se o 1º algarismo de n é igual ao seu último algarismo, o <br> 
    2º algarismo de n é igual ao penúltimo algarismo, e assim sucessivamente. <br>
    Exemplos: 567765 e 32423 são palíndromos. 567675 não é palíndromo.

<br>

13. Vamos escrever um programa que consiste em um Jogo de Adivinhação. O jogo funciona do seguinte modo: sorteia-se <br>
    um número inteiro aleatório entre 1 e 1000. Sua tarefa é tentar adivinhar o número sorteado através de "chutes".<br>
    A cada chute o programa deverá informar se o número "sorteado"é maior, menor ou igual ao número "chutado". <br>
    Quando o usuário acertar o número deverá ser impresso uma mensagem dizendo que ele acertou e a quantidade de <br>
    chutes dados. Para gerar números aleatórios entre 1 e 1000 use as seguintes instruções dentro do seu programa <br>
    Python. 
    
    ```python
    import random

    sorteado = random.randint(1,1001)
    ```

<br>

14. Dizemos que um inteiro positivo n é perfeito se for igual à soma de seus divisores positivos diferentes de n. <br>
    Exemplo: <br>
    6 é perfeito, pois 1 + 2 + 3 = 6.<br>
    12 não é perfeito, pois 1 + 2 + 3 + 4 + 6 = 16<br>
    28 é perfeito, pois 1 + 2 + 4 + 7 + 14 = 28<br>
    Sua tarefa será a de escrever um algoritmo em Python que, dado um inteiro positivo $n$, verificar se $n$ é perfeito.

<br>

15. Dados um inteiro n e uma seqüência de n números inteiros, determinar o comprimento de um segmento crescente de <br>
    comprimento máximo. <br>
    Exemplos: <br>
    Na sequência 5, 10, 3, <u>2, 4, 7, 9</u>, 8, 5 o comprimento do segmento crescente máximo é 4. <br>
    Na seqüência 10, 8, 7, 5, 2 o comprimento de um segmento crescente máximo é 1.

<br>

16. Uma das maneiras de evitar erros na digitação de números como conta corrente, CPF, boleto bancário é a utilização <br>
    de um ou mais dígitos de controle. Um dos métodos de cálculo é a utilização do método módulo 10. Segue a descrição <br>
    do algoritmo: Dado um número inteiro n devemos pegar cada dígito desse número começando pela casa das unidades e <br>
    multiplicar, alternadamente, por 2 e por 1. Caso o resultado da multiplicação seja um número maior ou igual a 10 <br>
    devemos simplificar esse valor somando os dois dígitos. Após feitas as multiplicações e as simplificações devemos <br>
    somar todos os valores e calcular o resto da divisão dessa soma por 10. Se o resto for 0 o dígito de controle é <br>
    zero, caso contrário o dígito de controle será 10 menos o resto. <br>
    A **Figura 1** pode servir de exemplo para o algoritmo móduto 10.

    ![Fig. 1. Trecho de boletodo Banco do Brasil](imgs/figura-1:-trecho-de-boleto-do-banco-do-brasil.png)

    Por exemplo vamos pegar o número do meio do boleto, o número corresponde a n = 246421501 e o dígito de controle <br>
    será 7. Vamos efetuar os seguintes cálculos:

        1 ∗ 2 = 2
        0 ∗ 1 = 0
        5 ∗ 2 = 10
        1 ∗ 1 = 1
        2 ∗ 2 = 4
        4 ∗ 1 = 4
        6 ∗ 2 = 12
        4 ∗ 1 = 4
        2 ∗ 2 = 4
        
    Daí somamos 2 + 0 + 1(1 + 0) + 1 + 4 + 4 + 3(1 + 2) + 4 + 4 = 23. O resto da divisão de 23 por 10 é 3 e como ele <br>
    é diferente de zero o dígito de controle de 246421501 será 7 (10 − 3). Escreva um algoritmo que lê um número <br>
    inteiro positivo e calcula o seu dígito de controle usando o método do módulo 10.

<br>

17. Em quase todas as linguagens existe um método/função que calcula a raiz quadrada de um número. Contudo, vamos <br>
    supor que na linguagem Python não exista tal método. Sua tarefa é tentar encontrar a raiz quadrada de um número <br>
    por tentativa e erro, ou seja, seu algoritmo recebe um número real $n > 0$ e tenta encontrar sua raiz quadrada. <br>
    Dica: pegue um número e eleve ao quadrado, caso ele fique "próximo" ao número $n$, significa que você encontrou a <br>
    raiz quadrada.
