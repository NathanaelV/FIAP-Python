# Recebe login e senha
login = input('Digite o login: ')
password = input('Digite a senha: ')

aux = f'{login} {password}'

# Verificar o conjunto senha e login
if aux == 'scott tiger' or aux == 'walt disney' or aux == 'spock ncc1701':
    print('Autenticado com sucesso')
else:
    print('Usuário ou senha inválidos')
