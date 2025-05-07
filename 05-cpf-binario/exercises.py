## ----- Exercícios CPFs ----- ##


## ----- Exercício 01 ----- ##

numero = int(input('Digite o CPF: '))
# numero = 11122233396 # 111.222.333-96
# numero = 74530297080 # 745.302.970-80
# numero = 31570283087 # 315.702.830-87

cpf = ''

while numero != 0:
    if numero > pow(10,10):
        cpf += f'-{numero % 100}'
        numero //= 100
    elif numero < 1000:
        cpf = f'{numero}{cpf}'
        numero //= 1000
    else:
        cpf = f'.{numero % 1000}{cpf}'
        numero //= 1000
    
print(cpf)



## ----- Exercício 02 ----- ##




## ----- Exercício 03 ----- ##

