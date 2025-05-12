n_products = int(input('Digite o número de produtos: '))

max_percent = -float('inf')
max_real = -float('inf')

for i in range(n_products):
    current_price = float(input(f'Digite o preço atual do {i+1}º produto: '))
    adjusted_price = float(input(f'Preço reajustado: '))

    real = adjusted_price - current_price
    percent = real / current_price

    if real > max_real:
        max_real = real
    
    if percent > max_percent:
        max_percent = percent

print(f'O maior aumento em reais foi R$ {max_real:.2f}')
print(f'O maior aumento percentual foi de {max_percent*100:.2f}%')
