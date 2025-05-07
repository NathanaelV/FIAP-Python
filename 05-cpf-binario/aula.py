# Vamos descascar os dígitos de um número:
# Esse é o mesmo algorismo que transforma números em decimais em binarios e vice e verça.

# numero = int(input('Digite um número: '))
# numero = 111222333 # 111.222.333-96
# numero = 745302970 # 745.302.970-80
# numero = 315702830 # 315.702.830-87
numero = 123123123 # 123.123.123-87
backup = numero

soma = 0
i = 2

while numero != 0:
    resto = numero % 10
    numero = numero // 10
    soma += resto * i
    i += 1

resto_soma = soma % 11

# print(resto_soma)

if resto_soma < 2:
    verificador1 = 0
else:
    verificador1 = 11 - resto_soma

print(f'Primeiro verificador {verificador1}.')

# Segundo verificador

numero = backup * 10 + verificador1
print(f'Novo teste: {numero}')
soma = 0
i = 2

print(numero)

while numero != 0:
    resto = numero % 10
    numero = numero // 10
    soma += resto * i
    i += 1

resto_soma = soma % 11

if resto_soma < 2:
    verificador2 = 0
else:
    verificador2 = 11 - resto_soma

print(f'Segundo verificador {verificador2}.')

print(f'CPF: {backup * 100 + verificador1 * 10 + verificador2}')


# OBS: Fazer o CPF de uma vez só, sem precisar usar o BACKUP. Fazer de uma vez só.
