def atualiza_valor(valor: int):
    valor = valor + 10

def atualiza_lista(info: list):
    info[0] = info[0] + 10

# Mutável
dado = [20, 30]
atualiza_lista(dado)
print(dado)

# Imutável
num = 20 
atualiza_valor(num)
print(num)


