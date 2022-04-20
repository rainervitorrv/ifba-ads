aluno = []

for i in range(1, 11):
    print(f'ALUNO {i} \n')

    boletim = []
    boletim.append(f'Aluno {i}')

    notas = []
    for x in range(1, 5):
        notas.append(
            float(input(f'Informe a {x}ª nota: '))
        )
    boletim.append(notas)

    somaNota = 0
    for nota in notas:
        somaNota += nota
    media = somaNota / len(notas)
    boletim.append(media)

    aluno.append(boletim)
    print('\n')


qtdAlunosAprovados = 0
for item in aluno:
    if(item[2] >= 7):
        qtdAlunosAprovados += 1
print(
    f'Existe o total de {qtdAlunosAprovados} alunos com a média maior ou igual a 7.0')
