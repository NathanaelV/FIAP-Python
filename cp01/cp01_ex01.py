# Receber as variáveis
valor_hora_aula = float(input('Digite o valor da hora aula: '))
num_aulas = int(input('número de aulas semanais: '))

salario_base = valor_hora_aula * num_aulas * 4.5
dsr = salario_base / 6
hora_atividade = (salario_base + dsr) * 0.05
salario_mensal = salario_base + dsr + hora_atividade

print(f'O salário base é R$ {salario_base:.2f}.')
print(f'O valor da hora-atividade é R$ {hora_atividade:.2f}.')
print(f'O DSR é R$ {dsr:.2f}.')
print(f'O salário mensal é R$ {salario_mensal:.2f}')
