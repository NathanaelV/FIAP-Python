banknote = int(input('Digite o valor da nota a ser trocada: '))
first_coin = int(input('Digite o valor da primeira moeda: '))
second_coin = int(input('Digite o valor da segunda moeda: '))

first_count = 0
second_count = 0

while banknote > 0:
    if banknote % second_coin == 0:
        second_count = banknote // second_coin
        banknote = 0
    else:
        banknote -= first_coin
        first_count += 1

if banknote == 0:
    print(f'{first_count} moeda(s) de {first_coin} e {second_count} moeda(s) de {second_coin}')
else:
    print('Não é possível fazer a troca')
