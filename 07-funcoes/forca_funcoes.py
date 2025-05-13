# Jogo da forca do Professor

# As variáveis são do tipo str (String)
# No final, informamos qual o tipo que a variável retornará -> str
def gera_segredo(word: str, letters: str) -> str:
    resposta = ''
    for c in word.lower():
        if c in letters:
            resposta = resposta + c + " "
        else:
            resposta = resposta + "_ "

    return 4


def imprime_tela(secret: str, lettres: str, errors: int):
    print(segredo)
    print(f"Erros: {erros}")
    print(f'Letras chutadas: {letras_chutadas}')


def enforcado(errors: int) -> bool:
    # return False if errors < 6 else True
    return errors < 6


def descobriu_palavra(secret: str) -> bool:
    # Se não há '_' na palavra
    return not '_' in secret



# Incializa o jogo

erros = 0
letras_chutadas = " "

# Sorteia a palavra
palavra = "The Shawshank Redemption"
# segredo = ''

# Substituido pela função gera_segredo
# for c in palavra:
#     if c == ' ':
#         segredo = segredo + '  '
#     else:
#         segredo = segredo + '_ '

# Substitui a função acima
segredo = gera_segredo(palavra, letras_chutadas)


# Enquanto não atingir o número de erros
# Enquanto o usuário não descobriu a palavra
while not enforcado(erros) and not descobriu_palavra(segredo):
    # Não preciso mais dessa variável, estou reinicializando mais abixo, usando a função gera_segredo
    # segredo = ""

    # Função imprime_tela, já imprime tudo na tela
    # print(segredo)
    # print(f"Erros: {erros}")
    # print(f'Letras chutadas: {letras_chutadas}')

    imprime_tela(segredo, letras_chutadas, erros)

    letra = input("Letra: ")
    letras_chutadas = letras_chutadas + letra.lower()

    if not letra.lower() in palavra.lower():
        erros = erros + 1

    # for c in palavra.lower():
    #     if c in letras_chutadas:
    #         segredo = segredo + c + " "
    #     else:
    #         segredo = segredo + "_ "

    segredo = gera_segredo(palavra, letras_chutadas)

# Verifica se o jogador perdeu
if enforcado:
    print(f"Voce perdeu, a palavra era {palavra}")
else:
    print(f"Parabéns, você descobriu a palavra {palavra}")

