# Lista de exercícios

from datetime import datetime


# 2

# name = input('Digite seu nome: ')
# last_name = input('Digite sue sobrenome: ')

# print(f'{last_name}, {name}')


# 3

# name = input('Digite seu nome: ')
# birth_date = int(input('Ano de nascimento: '))

# # age = 2025 - birth_date
# # Para manter o programa sempre atualizado
# age = datetime.now().year - birth_date

# print(f'{name} tem (ou terá) {age} anos neste ano.')


# 4
# num1 = int(input('Digite um número: '))
# num2 = int(input('Digite outro número: '))

# print(f'A soma dos dois numeros é {num1 + num2}')
# print(f'A multiplicação dos dois numeros é {num1 * num2}')
# print(f'A divisão inteira dos dois numeros é {num1 // num2}')
# print(f'O resto da divisão inteira dos dois numeros é {num1 % num2}')


# 5 
# num1 = float(input('Digite o primeiro número: '))
# num2 = float(input('Digite o segundo número: '))

# print(f'{num1} elevado a {num2} é igual a {num1**num2}')


# 6
# PI = 3.141592
# radius = float(input('Digite o raio da circuferência: '))

# print(f'A área é {PI * pow(radius,2)}')
# print(f'A circunferência é {2 * PI * radius}')


# 7
# num = int(input('Digite um número entre 0 e 99: '))

# tens = num // 10
# units = num % 10

# print(f'O número {num} tem {tens} dezenas e {units} unidades.')


# 8
# tshirts = int(input('Digite o número de camisetas: '))
# pants = int(input('Digite o número de calças: '))
# shoes = int(input('Digite o número de pares de sapato: '))

# combinations = tshirts * pants * shoes

# print(f'O número de combinações possíveis será {combinations}')


# 9
# price = float(input('Digite o valor do produto: '))
# discount = float(input('Digite a porcentagem do desconto: '))

# # Disconto
# final_price = price * (1 - discount * 0.01)

# # Aumento
# # final_price = price * (1 + discount * 0.01)

# print(f'O produto que custa R$ {price:.2f} com desconto de {discount}% ficará R$ {final_price}.')


# 10 
# distance = float(input('Digite a distância em metros: '))
# time = float(input('Digite o tempo em segundos: '))

# averange_speed = distance / time

# print(f'A velocidade média será {averange_speed:.2f} m/s ou {averange_speed * 3.6:.2f} km/h.')


# 11
# previous_salary = float(input('Digite o salário anterior: '))
# current_salary = float(input('Digite seu salário atual: '))

# salary_increase = current_salary / previous_salary - 1

# print(f'Você teve um aumento de {salary_increase * 100:.2f} % ')


# 12
# student_rm = int(input('Digite o RM: '))

# fifth = student_rm // 10000
# rest = student_rm % 10000

# fourth = rest // 1000
# rest = rest % 1000

# third = rest // 100
# rest = rest % 100

# second = rest // 10
# first = rest % 10

# sum = first + second + third + fourth + fifth

# print(f'A soma do RM será: {sum}')

# Exemplo do professor
# rm = int(input('Digite o RM: '))

# soma = 0
# resto = rm % 10
# soma += resto
# rm = rm // 10

# resto = rm % 10
# soma += resto
# rm = rm // 10

# resto = rm % 10
# soma += resto
# rm = rm // 10

# resto = rm % 10
# soma += resto
# rm = rm // 10

# resto = rm % 10
# soma += resto
# rm = rm // 10

# print(soma)


# 13
# nac_note = float(input('Digite a nota NAC: '))
# am_note = float(input('Digite a nota AM: '))
# ps_note = float(input('Digite a nota PS: '))

# average = (2*nac_note + 3*am_note + 5*ps_note) / 10

# print(f'A média do aluno é {average:.1f}')


# 14
# price = float(input('Digite o valor à vista: '))
# installments = float(input('Informe o valor da parcela: '))

# discount = (1 - price / (installments * 10)) * 100

# print(f'O valor do desconto, se pagar a vista, será de {discount:.1f}%')
