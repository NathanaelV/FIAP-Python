product = 'something'
highest_price = -float('inf')
highest_added_value = -float('inf')
name_price = ''
name_value = ''

while product != '':
    product = input('Digite o produto: ')
    if product != '':
        quantity = int(input('Quantidade: '))
        price = float(input('Preço: '))

        if highest_price < price:
            name_price = product
            highest_price = price
        
        if highest_added_value < price * quantity:
            name_value = product
            highest_added_value = price * quantity

print('\nResultado:')
print(f'O {name_price} é o produto com maior preço. R$ {highest_price}')
print(f'O {name_value} é o produto com maior valor agregado. R$ {highest_added_value}')

