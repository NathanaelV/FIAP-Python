# Métodos auxiliares
def posicao_da_letra(p_correta, letra, p_misteriosa):
    position = p_correta.find(letra)

    while position != -1:
        p_misteriosa = p_misteriosa[:position*2] + letra + p_misteriosa[position*2+1:]
        position = p_correta.find(letra, position + 1)
    
    return p_misteriosa


def gera_resposta(p_correta):
    resp = ''

    for i, c in enumerate(p_correta):
        resp += f'{p_correta[i]} '

    return resp


# Código principal

p_correta = 'piracicaba' 
erros = 0
p_misteriosa = '_ ' * len(p_correta)
p_resp = gera_resposta(p_correta)
tentativas_erradas = 'Tentativas: '

print('Começando o Jogo')
print(p_misteriosa)
print(f'Erros: {erros}/7')

while erros < 7 and p_misteriosa != p_resp:
    test = input('Digite uma letra: ').lower()

    if test in p_correta:
        print('\nMuito bom.')
        p_misteriosa = posicao_da_letra(p_correta, test, p_misteriosa)

    else:
        print('\nMenos uma vida')
        tentativas_erradas += f'{test} - '
        print(tentativas_erradas)
        erros += 1

    # print(f'Opção 2: {p_misteriosa != p_correta}')
    print(f"'{p_misteriosa}'")
    # print(f"'{p_resp}'")
    print(f'Erros: {erros}/7')
    print()

print('=' * 30)
print('Fim')
print(f'A Resposta é: {p_correta}\n')
