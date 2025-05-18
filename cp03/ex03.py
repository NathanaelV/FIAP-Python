
# ------ Using List ------ #

# print('\n Solução usando Lista:\n')
# tupla_names = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")
# names = list(tupla_names)

# while len(names) > 0:
#     first_name = names.pop(0)

#     for name in names:
#         print(f'{first_name} e {name}')



# ------ Without use List ------ #

tupla_names = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")

tupla_len = len(tupla_names)

first = 0
while first < tupla_len - 1:
    for n in range(first+1, tupla_len):
        print(f'{tupla_names[first]} e {tupla_names[n]}')

    first += 1
