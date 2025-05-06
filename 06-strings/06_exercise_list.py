# Lista de Exercício 04

## ----- Exercício 01 ----- ##

# str = input('Digite uma palavra: ')

# print(str.upper())



# ## ----- Exercício 02 ----- ##

# str = input('Digite uma palavra: ')

# resp = ''

# for i, c in enumerate(str):
#     resp += f'{str[i]} '

# print(f'{resp}.')



## ----- Exercício 03 ----- ##

# str = input('Digite uma palavra: ')
# letter = input('Digite a letra para substituir por "*": ').lower()

# resp = ''

# for c in str:
#     if c.lower() == letter:
#         resp += '*'
#     else:
#         resp += c

# print(resp)



## ----- Exercício 04 ----- ##

# phrase = input('Digite uma frase: ')
# letters = input('Digite as letras que deseja substituir: ').lower()

# resp = ''

# for c in phrase:
#     if c.lower() in letters:
#         resp += '*'
#     else:
#         resp += c

# print(resp)



## ----- Exercício 05 ----- ##

# phrase = input('Digite uma frase: ').upper()
# world = input('Digite a palavra: ').upper()

# position = phrase.find(world)
# count = 0

# while position != -1:
#     count += 1
#     position = phrase.find(world, position + 1)
    
# print(f'A palavra/letra {world} aparece {count} vez(es) na frase.')
