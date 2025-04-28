# Vamos descascar os dígitos de um número:
# Esse é o mesmo algorismo que transforma números em decimais em binarios e vice e verça.

numero = int(input('Digite um número: '))
backup = numero

soma = 0
i = 2

while numero != 0:
    resto = numero % 10
    numero = numero // 10
    soma = resto * i
    i += 1
    print(numero)
    print(f'Resto: {resto}')

soma 


# OBS: Fazer o CPF de uma vez só, sem precisar usar o BACKUP. Fazer de uma vez só.
