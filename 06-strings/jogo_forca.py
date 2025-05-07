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

    print(f"'{p_misteriosa}'")
    print(f'Erros: {erros}/7')
    print()

print('=' * 30)
print('Fim')
print(f'A Resposta é: {p_correta}\n')



## Resolução do Professor

# #incializa o jogo
# erros = 0
# letras_chutadas = " "
# #sorteia a palavra
# palavra = "The Shawshank Redemption"
# segredo = ''

# for c in palavra:
#     if c == ' ':
#         segredo = segredo + '  '
#     else:
#         segredo = segredo + '_ '

# while erros < 6 and "_" in segredo:
#     print(segredo)
#     segredo = ""
#     print(f"Erros: {erros}")
#     print(f'Letras chutadas: {letras_chutadas}')
#     letra = input("Letra: ")
#     letras_chutadas = letras_chutadas + letra.lower()

#     if not letra.lower() in palavra.lower():
#         erros = erros + 1

#     for c in palavra.lower():
#         if c in letras_chutadas:
#             segredo = segredo + c + " "
#         else:
#             segredo = segredo + "_ "

# if erros >= 6:
#     print(f"Voce perdeu, a palavra era {palavra}")
# else:
#     print(f"Parabéns, você descobriu a palavra {palavra}")
