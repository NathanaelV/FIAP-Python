def receives_students_grades(n_students):
    notes = []
    for n in range(n_students):
        note = float(input(f'Digite a nota do {n+1}º aluno: '))
        notes.append(note)
    return notes

def equal_or_less_than_average(notes, average_grades):
    count = 0
    for note in notes:
        if note <= average_grades:
            count += 1
    return count


n_students = int(input('Digite o número de alunos: '))

notes = receives_students_grades(n_students)
sum = sum(notes)

average_grades = sum / len(notes)

count = equal_or_less_than_average(notes, average_grades)

print('\nRelatório final: ')
print(f'- Média da turma: {average_grades}')
print(f'- Alunos na média ou abaixo da média: {count}')    
