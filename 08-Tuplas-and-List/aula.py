
## ----- Tuplas ----- ##

# Tuplas não são alteradas depois de criadas
estacoes = ('primavera', 'verão', 'outono', 'inverno')
semana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')

# É possível criar tuplas sem os ()
primos = 2, 3, 5, 7
print(primos)

# Mostra um item
print(f'Mostra um único elemento: `semana[3]` => {semana[3]}')

# Mostra uma Sub-tupla
print(f'Mostra uma Sub-tupla: semana[1:3] => {semana[1:3]}')

# Tipo
print(type(estacoes))

# Concatenação de Tuplas
perfeitos = (6, 28, 492)
numeros = primos + perfeitos
print(numeros)

# Quantidade de elementos
qtd = len(numeros)
print(f'A tupla numeros tem {qtd} elementos.')

# Loop
for n in numeros:
    print(n)



## ----- Listas ----- ##

print('\n\nListas:\n')

minhaLista = []                 # Criando lista vazia
minhaLista.append('Java')       # Adiciona no fim
minhaLista.append('Lógica')     # Adiciona no fim

print(minhaLista)

minhaLista.insert(0, 'Banco')   # Inserido na posição 0
print(minhaLista)

meusNumeros = [1, 4, 9]         # Cria lista com 3 elementos
meusNumeros.append(16)          # Adiciona um elemento
print(meusNumeros)              # Imprime o resultado

print(len(meusNumeros))         # Quantidade de elementos 
print(minhaLista[1])            # Mostra o elemento no index


print('\nFrutas:')
frutas = ['uva', 'kiwi', 'maça', 'caqui']
print(frutas)
frutas[2] = 'laranja'       # Substitui o elemento na posição 2 por laranja
print(frutas)

remove = frutas.pop(1)      # Remove o elemento na posição 1
print(f'O item `{remove}` foi removido, pela posição 1, de {frutas}')

print('del frutas[0]: Deleta o primeiro elemento')
del frutas[0]
print(frutas)

# Concatenação de listas
print('\nConcatenação de listas:')
individual = ['natação', 'tênis', 'judô']
coletivo = ['futebol', 'vôlei' , 'basquete']
esporte = individual + coletivo
print(esporte)

outros = ('Boxe', 'Golfe')

for esp in outros:
    individual.append(esp)

print(f'Individual: {individual}')
print(f'Esporte: {esporte}')