import math

# Lista de exercícios 02

## ----- Exercício 01 ----- ##

# num = float(input('Insira um número qualquer: '))

# if num > 10:
#     msg = 'maior'
# else:
#     msg = 'menor ou igual'

# print(f'O número {num} é {msg} que 10.')



## ----- Exercício 02 ----- ##

# num01 = int(input('Digite um número: '))
# num02 = int(input('Digite outro número: '))

# if num01 > num02:
#     msg = 'maior que'
# elif num01 == num02:
#     msg = 'igual a'
# else:
#     msg = 'menor que'

# print(f'{num01} é {msg} {num02}.')




## ----- Exercício 04 ----- ##

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



## ----- Exercício 05 ----- ##

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


# ----- Professor ----- #





## ----- Exercício 06 ----- ##

# num1 = int(input('Digite um número inteiro: '))
# num2 = int(input('Digite outro número inteiro: '))

# if num1 % num2 == 0:
#     msg = ''
# else:
#     msg = 'não '

# print(f'{num1} {msg}é divisível por {num2}.')


# ----- Professor ----- #

# num_a = int(input('Digite um número: '))
# num_b = int(input('Digite um número: '))

# match num_a % num_b:
#     case 0:
#         print(f'{num_a} / {num_b} tem resto Zero')
#     case _:
#         print(f'{num_a} / {num_b} não tem resto Zero')



## ----- Exercício 07 ----- ##

# num = float(input('Digite um número: '))

# if num < 0:
#     msg = 'Não há raiz quadrada para números negativos'
# else:
#     # round mostra até X casas decimais, porém esconde se for zero.
#     msg = f'A raiz de {num} é {round(math.sqrt(num), 4)}'

# print(msg)



## ----- Exercício 08 ----- ##

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



## ----- Exercício 09 ----- ##

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



## ----- Exercício 10 ----- ##

# print('Considerando uma equação de segundo grau como A.X² + B.X + C = 0.')
# a = float(input('Digite o valor de A: '))
# b = float(input('Digite o valor de B: '))
# c = float(input('Digite o valor de C: '))

# if a != 0:
#     delta = b ** 2 - 4 * a * c

#     if delta < 0:
#         print('Não existe raízes reais!')
#     elif delta == 0:
#         x = (-b + math.sqrt(delta)) / (2 * a)
#         print(f'Raizes X1 e X2 são iguais a {x}')
#     else:
#         x1 = (-b + math.sqrt(delta)) / (2 * a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)

#         print(f'A raiz x1 = {x1} e X2 = {x2}')
    
# else:
#     print('"A" não pode ser 0 (Zero)!')



## ----- Exercício 11 ----- ##

# price = float(input('Qual o valor do produto? '))

# print()
# print('-' * 70)
# print('Código\t| Condição de pagamento')
# print('-' * 70)
# print('1\t| A vista em dinheiro ou cheque, recebe 10% de desconto')
# print('2\t| A vista no cartão de crédito, recebe 5% de desconto')
# print('3\t| Em duas vezes, preço normal de etiqueta sem juros')
# print('4\t| Em quatro vezes, preço normal de etiquea mais juros de 7%')
# print('-' * 70)
# code = int(input('Código: '))
# print()

# match code:
#     case 1:
#         final_price = price * 0.9
#     case 2:
#         final_price = price * 0.95
#     case 3:
#         final_price = price
#     case 4:
#         final_price = price * 1.07
#     case _:
#         print('Escolha uma opção vália.')

# print(f'O valor final será R$ {final_price:.2f}')



## ----- Exercício 12 ----- ##

# first_media = float(input('Digite a média do primeiro semestre: '))
# second_media = float(input('Digite a média do segundo semestre: '))

# total_classes = int(input('Digite o número total de aulas: '))
# number_of_absences = int(input('Digite o número de faltas: '))

# final_media = first_media * 0.4 + second_media * 0.6

# presence = (total_classes - number_of_absences) / total_classes


# if final_media < 0 or final_media > 10:
#     print(f'A média {final_media} é inválida.')
# if presence < 0.7 or final_media <= 4:
#     print(f'Reprovado!\nNota: {final_media} - Presença: {presence * 100}%')
# elif presence > 0.7 and final_media <= 6:
#     print(f'Ficou de Exame!\nNota: {final_media} - Presença: {presence * 100}%')
# elif presence > 0.7:
#     print(f'Aprovado!\nNota: {final_media} - Presença: {presence * 100}%')



## ----- Exercício 13 ----- ##
