
## Problema 3.1 
# num = int(input('Digite um número inteiro: '))

# if num % 2 == 0:
#     print(f'{num} é par.')
# else:
#     print(f'{num} é impar.')

# Resolução em uma linha
# print(f"{num} é par." if num % 2 == 0 else f"{num} é impar.")



## Problema 3.2

# num = float(input('Digit um número: '))

# if num > 0:
#     print(f'\n{num} é um número positivo.\n')
# elif num < 0:
#     print(f'\n{num} é um número negativo.\n')
# else:
#     print('O número é zero.')



## Problama 3.3

# num1 = float(input('Digite um número: '))
# num2 = float(input('Digite outro número: '))
# sinal = input('Digite o sinal da operação que deseja fazer (+, -, / ou *): ')

# if sinal == '+':
#     print(f'{num1} + {num2} = {num1 + num2}')
# elif sinal == '-':
#     print(f'{num1} - {num2} = {num1 - num2}')
# elif sinal == '*':
#     print(f'{num1} * {num2} = {num1 * num2}')
# elif sinal == '/':
#     if num2 != 0:
#         print(f'{num1} / {num2} = {num1 / num2}')
#     else:
#         print(f'O segundo número não pode ser Zero na divisão.')

# Exemplo do professor

# num1 = float(input('Digite um número: '))
# num2 = float(input('Digite outro número: '))
# sinal = input('Digite o sinal da operação que deseja fazer (+, -, / ou *): ')

# if sinal == '+':
#     resp = num1 + num2
# elif sinal == '-':
#     resp = num1 - num2
# elif sinal == '*':
#     resp = num1 * num2
# elif sinal == '/':
#     if num2 != 0:
#         resp = num1 / num2
#     else:
#         print(f'O segundo número não pode ser Zero na divisão.')
#         resp = None
# else:
#     print('Operador invalido!')
#     resp = None

# if resp != None:
#     print(f'Resultado: {num1} {sinal} {num2} = {resp}.')

# Using match/case

# num1 = float(input('Digite um número: '))
# # strip remove os espaços em brancos no começo e no final da String
# op = input('Digite o operador (+, -, *, /): ').strip()
# num2 = float(input('Digite outro número: '))

# match op:
#     case '+':
#         print(f'{num1} + {num2} = {num1 + num2}')
#     case '-':
#         print(f'{num1} - {num2} = {num1 - num2}')
#     case '*':
#         print(f'{num1} * {num2} = {num1 * num2}')
#     case '/':
#         if num2 != 0:
#             print(f'{num1} / {num2} = {num1 / num2}')
#         else:
#             print('Não divisão por Zero.')
#     case _:
#         print('Escolha um operador válido.')



## Problema 3.4

# salary = float(input('Digite o seu salário: '))

# if salary <= 1_693.72:
#     value = salary * 0.08
# elif salary <= 2_822.90:
#     value = salary * 0.09
# elif salary <= 5_645.80:
#     value = salary * 0.11
# else:
#     value = 5_645.80 * 0.11

# print(f'O valor será de R$ {value:.2f}.')



## Problema 3.5

# first, second, third = 0, 0, 0
# num1 = int(input('Digiete um número: '))
# num2 = int(input('Digiete outro número: '))
# num3 = int(input('Digiete mais um número: '))

# if num1 <= num2 and num2 <= num3:
#     first, second, third = num3, num2, num1
# elif num2 <= num1 and num1 <= num3:
#     first, second, third = num3, num1, num2
# elif num1 <= num3 and num3 <= num2:
#     first, second, third = num2, num3, num1
# elif num3 <= num1 and num1 <= num2:
#     first, second, third = num2, num1, num3
# elif num3 <= num2 and num2 <= num1:
#     first, second, third = num1, num2, num3
# else:
#     first, second, third = num1, num3, num2

# print(f'\nA ordem do maior para o menor é: {first}, {second} e {third}.\n')
