# Recebe os lados dos triânguos

a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

# Verifica se é um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    
    # Identifica o tipo do triângulo
    if a == b == c:
        print('Triângulo Equilátero')
    elif a == b or b == c or c == a:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')

else:
    print('Não é um triângulo')
