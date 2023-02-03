# sorteia a ordem que os alunos irão apresentar o trabalho

from random import randrange
alunos = ['Roberto', 'Paulo', 'Maria', 'Joaquina']
n = 1
while len(alunos) != 0:
    aluno = alunos[randrange(0, len(alunos))]
    print('O {}o aluno que irá apresentar o trabalho será "{}".'.format(n, aluno))
    alunos.remove(aluno)
    n += 1
