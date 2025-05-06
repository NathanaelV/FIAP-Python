# Computational Thinking Using PYTHON

Aqui terá os exercícios propostos durante as aulas de Python.

Resoluções do professor: https://github.com/egondo/1tdsr

## Lista de Exercício 4

1.  Crie um programa em Python que recebe uma String e retorna uma outra String com os mesmos caracteres só que em caixa <br>
    alta. Por exemplo: se a palavra for `"Melancia"`, seu programa deverá retornar `"MELANCIA"`.

<br>

2.  Crie um programa que imprime uma String contendo os caracteres da entrada palavra separados por espaços. <br>
    Por exemplo, se a entradao for a palavra `"Manga"`, seu programa deverá imprimir `"M a n g a "`.

<br>

3.  Escreva um programa que recebe duas Strings: `frase` e `letra`; a `frase` representa um conjunto de caracteres e `letra` <br>
    um único caracter. Sua função deverá substituir toda ocorrência do caracter `letra` contido `frase` pelo caracter `*`. <br>
    Por exemplo, se frase for `"Jabuticaba"` e a letra for "a"então seu método deverá retornar `"J*butic*b*"`. Note que, <br>
    seu programa deverá funcionar independente da letra ser maiúscula ou minúscula, ou seja, toda letra `"a"` e `"A"` deve <br>
    ser substituída. Considere que não há caracteres acentuados nas palavras e não deve ser usado o método `replace` <br>
    neste exercício.

    | *OBS: Faça a validação da letra para que seja apenas um único caracter.*

<br>

4.  Escreva um programa que recebe duas Strings: `frase` e `letras`; a frase representa um conjunto de caracteres e <br>
    `letras` alguns caracteres. Seu programa deverá substituir cada caracter c contido na `frase` pelo caracter `*` <br>
    se este caracter `c` estiver presente em `letras`. <br>
    Por exemplo, se a frase for: <br>

    ```
    I can only show you the door.
    You’re the one that has to walk through it.
    ```

    e letras for aro então seu método deverá retornar: 

    ```
    I c*n *nly sh*w y*u the d***.
    Y*u’re the one th*t h*s t* w*lk th**ugh it
    ```

    Note que, seu programa deverá funcionar independente da letra ser maiúscula ou minúscula, ou seja, toda letra `"a"` <br>
    e `"A"` deve ser substituída e considere que não há caracteres acentuados nas palavras.

<br>

5.  Dados duas strings (um contendo uma frase e outro contendo uma palavra), determine o número de vezes que a palavra <br>
    ocorre na frase. Exemplo: Para a palavra ANA e a frase:

    ```
    ANA E MARIANA GOSTAM DE BANANA
    ```

    Temos que a palavra ocorre 4 vezes na frase. Escreva um programa que resolve o problema acima, seu programa deverá <br>
    receber as duas strings e retornar o número de ocorrências da palavra na frase.

    *Sugestão: use o método find da String.*
