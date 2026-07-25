def aprovacao(nota):
    if nota > 6:
        return 'Aprovado'
    if nota < 4:
        return 'Reprovado'
    if nota >= 4 and nota <= 6:
        return 'Recuperação'

nota=float(input('Digite a nota do aluno:'))
print(aprovacao(nota))

