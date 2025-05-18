n_products = int(input('Digite o número de produtos: '))

max_percent = -float('inf')
max_real = -float('inf')

for i in range(n_products):
    print(f"\nProduto {i + 1}:")
    current_price = float(input(f'Preço atual: '))
    adjusted_price = float(input(f'Preço reajustado: '))

    real = adjusted_price - current_price
    percent = real / current_price

    if real > max_real:
        max_real = real
    
    if percent > max_percent:
        max_percent = percent

print("\n--- RESULTADO FINAL ---")
print(f'O maior aumento em reais foi R$ {max_real:.2f}')
print(f'O maior aumento percentual foi de {max_percent*100:.2f}%')
