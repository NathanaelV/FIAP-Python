import math

num = 10
half_num = num // 2
num_faq = math.factorial(num)
half_num_faq = math.factorial(half_num)

resp = num_faq / (pow(2, half_num) * half_num_faq)
print(int(resp))

names = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")

