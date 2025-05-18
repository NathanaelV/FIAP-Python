string = input('Digite uma palavra/frase: ')

reverse_string = ''

for c in string:
    reverse_string = c + reverse_string

print(reverse_string)

# Ou 

reverse_string = string[::-1]
print(reverse_string)
