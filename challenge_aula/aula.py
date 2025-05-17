def cadastra_pergunta(repositorio: list):
    numero = int(input('Número: '))
    enunciado = input('Enunciado: ')
    tipo = input('Tipo: ')
    if tipo == 'unica' or tipo == 'multipla':
        alternativas = []
        print("Alternativas ou Enter para finalizar")
        num = 1
        item = input(f'alternativa {num}: ')
        while item != '':
            alternativas.append(item)
            num += 1
            item = input(f'alternativa {num}: ')
    else:
        alternativas = None
    
    repositorio.append(numero)
    repositorio.append(enunciado)
    repositorio.append(tipo)
    repositorio.append(alternativas)

def menu() -> int:
    print('\n1) Cadastra Pergunta')
    print('2) Aplica enquete')
    print('3) Visualiza perguntas')
    print('4) Apaga pergunta')
    print('5) Sair')
    return int(input('Opção: '))

def apaga_perguntas(repositorio: list):
    num = int(input('Digite o nº da pergunta que deseja apagar'))
    i = 0
    while i < len(repositorio) and repositorio[i] != num:
        i = i + 4

    if repositorio[i] == num:
        repositorio.pop(i)
        repositorio.pop(i)
        repositorio.pop(i)
        repositorio.pop(i)


# main
perguntas = []

op = 0
while op != 5:
    op = menu()
    match op:
        case 1:
            cadastra_pergunta(perguntas)
        case 2:
            print('Aplicando a enquete')
        case 3:
            print(perguntas)
        case 4:
            apaga_perguntas(perguntas)
        case 5:
            print('Até a próxima')
        case _:
            print('Opção inválida!')




