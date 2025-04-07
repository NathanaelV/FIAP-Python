# Computational Thinking Using PYTHON

Aqui terá os exercícios propostos durante as aulas de Python.

## Problemas

**3.1** Um número inteiro pode ser par ou ímpar. Escreva um algoritmo que recebe números inteiro e <br>
imprimi na tela a informação sobre sua paridade.

<br>

**3.2** Escreva um algoritmo que recebe um número e imprime na tela a informação que o número é <br>
positivo, negativo ou igual a zero.

<br>

**3.3** Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações <br>
matemáticas(`+`, `-`, `*`, `/`)) e calcula o valor da operação matemática, ou seja, se a entrada for <br>
5, ∗ e 6 então seu programa deverá mostrar 30.

<br>

**3.4** Escreva um algoritmo que lê o salário de um funcionário e mostra qual o percentual de desconto <br>
que será apcliado para usa contribuição ao INSS. Use a tabela abaixo para calcular o desconto:

| Salário Contribuição           | Alíquota/Valor                     |
|--------------------------------|------------------------------------|
| Até R$ 1.693,72                | 8%                                 |
| De R$ 1.693,73 até R$ 2.822,90 | 9%                                 |
| De R$ 2.822,91 até R$ 5.645,80 | 11%                                |
| Acima de R$ 5.645,80           | 11% sobre R$ 5.645,80              |

Por exemplo, um trabalhador com salário de R$ 2.000,00 o percentual de desconto será de 9%. <br>
Quem ganha R$ 8.000,00 terá um desconto de 11% sobre o teto da aposentadoria.

<br>

**3.5** Escreva um algoritmo que recebe três números inteiros e imprime eles em ordem crescente.

<br>

---

## Lista de Exercício 2

1. Faça um algoritimo que receba um número e mostre uma mensagem caso este número seja maior que 10.

<br>

2. Excrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se <br>
houve um empate.

<br>

3. Não tem na lista

<br>

4. Escreva um algoritmo para ler o nome de 2 times e o número de gosl marcados em uma partida. <br>
Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a palavra **EMPATE**.

<br>

5. A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha trabalhado <br>
além da jornada mensal exigida, ele terá direito a receber hora-extra. O valor da hora-extra é o <br>
valor que ele recebe por hora acrescido de 50%. Supondo que ele trabalhe apenas nos dias úteis, <br>
escreva um algoritmo que recebe:

    a) o total de dias úteis de um mês

    b) o total de horas trabalhadas pelo trabalhador

    c) quanto o trabalhador recebe por hora

    Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário final do trabalhador.

<br>

6. Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.

<br>

7. A raiz quadrada é uma operação que apenas aceita números positivos. Escreva um algoritmo <br>
que lê um número qualquer e retorna a raiz quadrada desse número se possível. Use a função <br>
`math.sqrt(<numero>)` para calcular a raiz quadrada em Python. Note que, para usar essa função,<br>
você terá que importar o módulo **math** antes.

    ```python
    import math

    #coloque aqui o resto do seu codigo
    #tudo na frente do sustenido eh
    #considerado um comentario em Python
    ```

<br>

8. Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a <br>
tabela a seguir:

    | Categoria     | Idade         |
    |---------------|---------------|
    | Infantil      | 5 a 7         |
    | Juvenil       | 8 a 10        |
    | Adolescente   | 11 a 15       |
    | Adulto        | 16 a 30       |
    | Senior        | acima de 30   |

<br>

9. No exercício da calculadora, visto em sala de aula, temos um problema com a operação <br>
de divisão. Sua tarefa será exibir uma mensagem informando que é impossível fazer uma <br>
divisão por 0. Note que, essa mensagem só deverá aparecer quando o usuário quiser fazer <br>
tal operação.

<br>

10. Uma equação de 2º grau é da forma: $ax^2 + bx + c = 0$, onde a ̸= 0. Escreva um algoritmo <br>
que recebe os três coeficientes da equação, calcula e imprime as raízes reais se for possível. <br>
Use a seguinte fórmula para resolver a equação:

    $∆ = b^2 − 4ac$ <br>
    $x1 = (−b + √∆) / 2a$ <br>
    $x2 = (−b − √∆) / 2a$

<br>

11. Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço <br>
normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir <br>
para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

    | código    | condição de pagamento                                     |
    |-----------|-----------------------------------------------------------|
    |1          |A vista em dinheiro ou cheque, recebe 10% de desconto      |
    |2          |A vista no cartão de crédito, recebe 5% de desconto        |
    |3          |Em duas vezes, preço normal de etiqueta sem juros          |
    |4          |Em quatro vezes, preço normal de etiqueta mais juros de 7% |

<br>

12. Faça um algoritmo que leia as médias semestrais obtidas por um aluno na disciplina de <br>
Computational Thinking, o número de aulas ministradas e o número de aulas assistidas por <br>
este aluno nesta disciplina. Calcule e mostre a média final deste aluno e diga se ele foi <br>
aprovado ou reprovado ou está de exame. Lembrando que a média do primeiro semestre tem <br>
peso 4 e a do segundo peso 6, além disso, o aluno tem que ter frequentado mais de 70% das <br>
aulas.

<br>

13. Desenvolva um algoritmo que informe se uma data é válida ou não. O algoritmo deverá ler <br>
2 números inteiros, que representem o dia e o mês e informar se é um dia do mês válido. <br>
Desconsidere os casos de ano bissexto, ou seja, fevereiro têm 28 dias.

<br>

14. Agora, vamos acrescentar na verificação de data os casos de ano bissexto, ou seja, o ano que <br>
fevereiro tem 29 dias. Um ano é bissexto se:

    a) o ano for divisível por 4 <br>

    b) anos múltiplos de 100, não são bissextos <br>

    c) quando o ano for divisível por 400 ele é bissexto <br>

    d) as últimas regras prevalecem sobre as primeiras <br>

    Para exemplificar um pouco essas regras, observe que 1900 não foi bissexto mas 2000 foi.

