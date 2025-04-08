# Usando o Match/case:

num1 = float(input('Digite um número: '))
# strip remove os espaços em brancos no começo e no final da String
op = input('Digite o operador (+, -, *, /): ').strip()
num2 = float(input('Digite outro número: '))

match op:
    case '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    case '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    case '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    case '/':
        if num2 != 0:
            print(f'{num1} / {num2} = {num1 / num2}')
        else:
            print('Não divisão por Zero.')
    case _:
        print('Escolha um operador válido.')
