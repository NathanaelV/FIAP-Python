# # 4.1

# print('\n-- Soma de 5 números inteiros --')
# sum = 0

# # # Usando o For:
# # for i in range(5):
# #     num = int(input('Digite um número: '))
# #     sum += num

# # Usando o While:
# i = 0
# while i < 5:
#     num = int(input('Digite um número: '))
#     sum += num
#     i += 1


# print(f'A soma é {sum}.\n')



# # 4.2

# print('\n-- Tabuada de um número --')

# num = int(input('Digite o número que deseja mostrar a tabuada: '))

# Usando o While:
# i = 1
# while i <= 10:
#     print(f'{num} x {i:2} = {num * i}')
#     i += 1

# # # Usando For:
# # for i in range(1, 11):
# #     print(f'{num} x {i:2} = {num * i}')



# # 4.3

# print('\n-- Mostra N números na tela --')

# num = int(input('Digite um número inteiro: '))

# # Usando o While:
# # i = 1
# # while i <= num:
# #     print(i)
# #     i += 1

# # Usando o For:
# for i in range(1, num+1):
#     print(i)



# # 4.4

# print('\n-- Média de 2 notas com validação --')

# sum = 0

# note = float(input('Digite a 1ª Nota: '))

# while note < 0 or note > 10:
#     note = float(input('Digite uma nota válida! Digite a 1ª Nota: '))

# sum += note

# note = float(input('Digite a 2ª Nota: '))

# while note < 0 or note > 10:
#     note = float(input('Digite uma nota válida! Digite a 2ª Nota: '))

# sum += note

# print(f'A média será {sum / 2:.2}\n')



# 4.5

# print('\n-- Calcula a soma dos n primeiros números --')

# n = int(input('Digite um número: '))

# while n <= 0:
#     n = int(input('Digite um número positivo: '))

# sum = 0
# i = 0

# # Usando o For:
# # for i in range(1,num+1):
# #     sum += i

# # Usando o While:
# while i < n:
#     i += 1
#     sum += i
#     print(i, end='') if i == n else print(f'{i} ', end='+ ')

# print(f' = {sum}\n')



# 4.6

# print('\n-- Divisores de um número --')

# num = int(input('Digite um número inteiro: '))

# i = 1
# while i <= num:
#     if num % i == 0:
#         if num != i:
#             print(f'{i}', end=', ')
#         else:
#             print(f'{i}\n')
#     i += 1

