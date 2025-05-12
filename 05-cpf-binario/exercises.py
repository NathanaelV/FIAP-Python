## ----- Exercícios CPFs ----- ##


## ----- Exercício 01 ----- ##

# numero = int(input('Digite o CPF: '))
# # numero = 11122233396 # 111.222.333-96
# # numero = 74530297080 # 745.302.970-80
# # numero = 31570283087 # 315.702.830-87

# cpf = ''

# while numero != 0:
#     if numero > pow(10,10):
#         cpf += f'-{numero % 100}'
#         numero //= 100
#     elif numero < 1000:
#         cpf = f'{numero}{cpf}'
#         numero //= 1000
#     else:
#         cpf = f'.{numero % 1000}{cpf}'
#         numero //= 1000
    
# print(cpf)



## ----- Exercício 02 ----- ##




## ----- Exercício 03 ----- ##

# numero = int(input('Digite o CPF: '))
# # numero = 111222333 # 111.222.333-96
# # numero = 745302970 # 745.302.970-80
# # numero = 315702830 # 315.702.830-87

# while len(str(numero)) < 11:
#     backup = numero
#     i = 2
#     soma = 0

#     while numero != 0:
#         resto = numero % 10
#         numero //= 10
#         soma += resto * i
#         i += 1

#     prov = soma % 11

#     if prov < 2:
#         verificador = 0
#     else:
#         verificador = 11 - prov

#     numero = backup * 10 + verificador

# print(numero)



## ----- Exercício 04 ----- ##

# numero = int(input('Digite o CPF: '))
numero = 11122233396 # 111.222.333-96
# numero = 74530297080 # 745.302.970-80
# numero = 31570283087 # 315.702.830-87

test = numero // 100

print(test)

while len(str(test)) < 11:
    backup = test
    i = 2
    soma = 0

    while test != 0:
        resto = test % 10
        test //= 10
        soma += resto * i

    prov = soma % 11

    if prov < 2:
        verificador = 0
    else:
        verificador = 11 - prov

    test = backup * 10 + verificador

print(test)
