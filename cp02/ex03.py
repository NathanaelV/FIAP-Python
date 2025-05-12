n_num = int(input('Digite quantos números deseja inserir: '))

sum_above_50 = 0
count_less_than_100 = 0

for i in range(n_num):
    num = float(input('Digite o número: '))

    if num > 50:
        sum_above_50 += num
    
    if num < 100:
        count_less_than_100 += 1
    
print(f'Na sequência passada:')
print(f'- A soma dos número acima de 50 foi {sum_above_50}.')
print(f'- Teve {count_less_than_100} numero(s) menores que 100.')
