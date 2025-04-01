import math

# Lista de exercícios 02

## Exercício 01

# num = float(input('Insira um número qualquer: '))

# if num > 10:
#     msg = 'maior'
# else:
#     msg = 'menor ou igual'

# print(f'O número {num} é {msg} que 10.')



## Exercício 02

# num01 = int(input('Digite um número: '))
# num02 = int(input('Digite outro número: '))

# if num01 > num02:
#     msg = 'maior que'
# elif num01 == num02:
#     msg = 'igual a'
# else:
#     msg = 'menor que'

# print(f'{num01} é {msg} {num02}.')




## Exercício 04

# team01 = input('Digite o nome do primeiro time: ')
# team01_goals = int(input('Digite o número de goals que esse time marcou: '))

# team02 = input('Digite o nome do segundo time: ')
# team02_goals = int(input('Digite o número de goals que esse time marcou: '))

# if team01_goals == team02_goals:
#     msg = 'Foi EMPATE.'
# else:
#     if team02_goals < team01_goals:
#         msg2 = team01
#     else:
#         msg2 = team02
#     msg = f'O team vencedor foi {msg2}.'

# print(msg)



## Exercício 05

# days = int(input('Digite o número de dias úteis: '))
# hours_worked = int(input('Número de total de horas trabalhadas do trabalhador: '))
# wage = float(input('Digite o valor da hora do trabalhador: '))

# total_hours = days * 8
# overtime = hours_worked - total_hours
# salary = total_hours * wage
# overtime_msg = ''

# if overtime > 0:
#     overtime_wage = overtime * wage * 1.5
#     overtime_msg = f' R$ {overtime_wage:.2f} são de hora(s) extra.'
#     salary += overtime_wage

# msg = f'O salário será R$ {salary:.2f}.{overtime_msg}'

# print(msg)



## Exercício 06

# num1 = int(input('Digite um número inteiro: '))
# num2 = int(input('Digite outro número inteiro: '))

# if num1 % num2 == 0:
#     msg = ''
# else:
#     msg = 'não '

# print(f'{num1} {msg}é divisível por {num2}.')



## Exercício 07

# num = float(input('Digite um número: '))

# if num < 0:
#     msg = 'Não há raiz quadrada para números negativos'
# else:
#     # round mostra até X casas decimais, porém esconde se for zero.
#     msg = f'A raiz de {num} é {round(math.sqrt(num), 4)}'

# print(msg)



## Exercício 08

# age = int(input('Digite a idade do jogador: '))

# if age < 0:
#     category = 'Digite uma idade válida.'
# elif age >= 0 and age < 5:
#     category = 'Muito novo para nadar'
# elif age < 8:
#     category = 'Infantil'
# elif age < 11:
#     category = 'Juvenil'
# elif age < 16:
#     category = 'Adolescente'
# elif age < 30:
#     category = 'Adulto'
# else:
#     category = 'Senior'


# print(category)



## Exercício 09

# num1 = float(input('Digite um número: '))
# op = input('Qual operação deseja fazer (+, -, *, /): ')
# num2 = float(input('Digite o segundo número: '))

# match op:
#     case '+':
#         resp = num1 + num2
#     case '-':
#         resp = num1 - num2
#     case '*':
#         resp = num1 * num2
#     case '/':
#         if num2 != 0:
#             resp = num1 / num2
#         else:
#             print('Não há divisão por Zero.')
#             resp = None
#     case _:
#         print('Operador não definido!\nDigite um operador válido!')
#         resp = None

# if resp != None:
#     print(f'{num1} {op} {num2} = {resp}')



## Exercício 10

