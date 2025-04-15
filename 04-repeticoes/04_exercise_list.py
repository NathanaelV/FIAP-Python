import math

# Lista de exercícios 04

## ----- Exercício 01 ----- ##

# num = None
# sum = 0

# while num != 0:
#     num = int(input('Digite um número inteiro: '))
#     sum += num

# print(f'Soma = {sum}')



## ----- Exercício 02 ----- ##

# students = int(input('Digite o número de alunos: '))

# i = 0
# sum = 0

# while i < students:
#     i += 1
#     note = float(input(f'Digite a nota do {i}º aluno: '))
#     sum += note

# average = sum / i

# print(f'A média da turma é: {average}')



## ----- Exercício 03 ----- ##

# students = int(input('Digiete o número de alunos: '))

# count = 0
# sum = 0
# notes_greater_than_5 = 0
# notes_lower_than_5 = 0

# while count < students:
#     note = float(input('Digite a nota do aluno: '))
#     sum += note
#     count += 1

#     if note < 5:
#         notes_lower_than_5 += 1
#     else:
#         notes_greater_than_5 += 1

# avengare = sum / students

# print(f'Média da turma: {avengare}')
# print(f'Quantidae de alunos com nota menor que 5: {notes_lower_than_5}')
# print(f'Quantidae de alunos com nota maior que 5: {notes_greater_than_5}')



## ----- Exercício 04 ----- ##

# n = int(input('Digite a quantidade de números que será digitada: '))

# count = 0
# positives = 0
# negatives = 0
# zeros = 0

# while count < n:
#     num = float(input('Digite um número qualquer: '))
    
#     if num > 0:
#         positives += 1
#     elif num < 0:
#         negatives += 1
#     else:
#         zeros += 1

# print(f'Negativos: {negatives}')
# print(f'Positivos: {positives}')
# print(f'Zeros: {zeros}')



## ----- Exercício 05 ----- ##

# num = int(input('Digite um número inteiro: '))

# i = 1
# text = ''

# while i <= num / 2:
#     if num % i == 0:
#         text += f'{i} '
#     i += 1

# print(text)



## ----- Exercício 06 ----- ##

# i = 0
# bad = 0
# regular = 0
# good = 0
# candidates = 20

# while i < candidates:
#     note = int(input('Digite a nota do candidato: '))

#     if note > 0 and note <= 20:
#         bad += 1
#     elif note <= 50:
#         regular += 1
#     elif note <= 70:
#         good += 1

#     i += 1

# bad_percent = bad / candidates * 100
# regular_percent = regular / candidates * 100
# good_percent = good / candidates * 100

# print(f'Notas até 20 pontos: {bad_percent:.2f}%')
# print(f'Notas de 21 até 50 pontos: {regular_percent:.2f}%')
# print(f'Notas de 51 até 70 pontos: {good_percent:.2f}%')



## ----- Exercício 07 ----- ##

# fahrenheit = 50

# while fahrenheit <= 150:
#     celcius = (fahrenheit - 32) * 5 / 9
#     print(f'{fahrenheit} \t {celcius:.2f}')
#     fahrenheit += 1



## ----- Exercício 08 ----- ##

num = int(input('Digite um número: '))

i = 3

if num < 2 or (num != 2 and num % 2 == 0):
    texto = 'Não é primo'
else:
    texto = 'É primo'
    limit = math.ceil(math.sqrt(num))

    while i <= limit:
        if (num % 2 == 0 or num % i == 0) and num != 2:
            texto = 'Não é primo'
            break
        i += 2

print(texto)
