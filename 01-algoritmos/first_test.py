import random

# def sum(a,b):
#     return a + b

# a = 15
# b = 32
# print(sum(a,b))

# Atividade 1
# total = 0
# num = int(input("Enter a number: "))

# while num != 0:
#     total += num
#     num = int(input("Enter a number: "))
#     print(total)

# print(total)


# Atividade 2

# productPrice = int(input("Enter the product price: "))
# discount = int(input("Enter the discount (%): "))

# # productPrice = productPrice - productPrice * discount / 100
# productPrice = productPrice * (1 - discount / 100)

# print(productPrice)


# Atividade 3

# numbers = [random.randint(-100,100) for _ in range(10)]
# biggest_number = 0

# for i, number in enumerate(numbers):
#     if i == 0:
#         biggest_number = number
#     elif number >= biggest_number:
#         biggest_number = number

# print(f"In {numbers}\nThe biggest number is {biggest_number}")


# Atividade 4

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de c: "))

delta = pow(b,2) - 4*a*c

if delta < 0:
    print('Não há raízes reais')

elif delta == 0:
    x = -b / (2*a)
    print(f"As raízes são iguais a {x}")

elif delta > 0:
    x1 = (-b + pow(delta, 0.5)) / (2*a)
    x2 = (-b - pow(delta, 0.5)) / (2*a)
    print(f'Teremos duas raízes reais. X1: {x1}; X2: {x2}')

